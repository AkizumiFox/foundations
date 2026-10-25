"""Chapter and section pointers in prose and in the bookkeeping: find them, renumber them, mask them.

A **prose pointer** is what the reader sees: "Chapter 4", "Chapters 1–3", "Section 4.7",
"Sections 4.3 to 4.6". Inside one volume it uses the volume's own numbers; a pointer into another
volume names that volume the way the engine prints a reference into another book ("Logic and
Proof, Theorem 4.2.1"), with the title in italics:

    *Logic and Proof*, Chapter 4          *Logic and Proof*, Section 4.7
    *Logic and Proof*, Chapters 3–5, and *Sets and Functions*, Chapters 1–3

A **bookkeeping pointer** is what the author and the tools read (STATUS.md, NOTATION.md,
blueprints, dependency ledgers): the atlas chapter id, which does not change when a volume is
renumbered: `F1.4`, `F1.4 §07`, `F1.3–F2.3`.

* `rewrite_prose(text, mapping, here)` and `rewrite_atlas(text, mapping)` renumber every pointer of
  a text whose numbers are those of an old numbering (`mapping`: old chapter number -> (volume
  prefix, local number, atlas id)); code, math and inline code are left alone. Used once to split
  analysis-book into volumes, and again whenever a volume is renumbered.
* `mask(text)` replaces every pointer by one token, for hashing: the claim ledger
  (tools/ledger.py) hashes masked text, so renumbering (or moving a label into another book,
  `@label` -> `@fd1:label`) does not stale a referee's verdict. The price, as with usage forms: a
  verdict also survives an edit that only changes which chapter a pointer names.
"""
import re

DASH_CHARS = r"(?:–|—|-|to)"
DASH = rf"\s*{DASH_CHARS}\s*"
SEP_IN = rf"(?:{DASH}|\s*,\s*|\s+and\s+|\s+or\s+)"
CH_NUM = r"\d+(?!\.\d)"
SEC_NUM = r"\d+\.\d+"
CHAPTERS = re.compile(rf"\b(Chapters?)\s+({CH_NUM}(?:{SEP_IN}{CH_NUM})*)\b")
SECTIONS = re.compile(rf"\b(Sections?)\s+({SEC_NUM}(?:{SEP_IN}{SEC_NUM})*)\b")
# Ch 4, Ch. 4, ch04 (not ch04-slug, ch04/, ch04.md, nor "ch. 5" of a source book)
CH_ABBR = re.compile(r"\bCh\.?\s?(\d{1,2})\b(?![-/]|\.\d)|\bch(\d{2})\b(?![-/\w]|\.\w)")
TITLED = re.compile(r"\*([^*\n]{1,160}?)\*,\s+(?=(?:Chapters?|Sections?)\s+\d)")
ATLAS_ID = re.compile(r"\b[A-Z]{1,3}\d?\.\d+[ab]?\b")
COMPANION = re.compile(r"companion|linear[- ]algebra", re.I)


# ---------------------------------------------------------------------------
# Regions: what is prose
# ---------------------------------------------------------------------------

def protected_spans(text: str) -> list:
    """(start, end) of code fences, display and inline math, and inline code."""
    spans = []
    pos = 0
    fence = None
    for line in text.splitlines(keepends=True):
        s = line.strip()
        m = re.match(r"(`{3,}|~{3,})", s)
        if fence is None and m:
            fence = (m.group(1)[0], len(m.group(1)), pos)
        elif fence is not None and s.startswith(fence[0] * fence[1]) and not s.strip(fence[0]):
            spans.append((fence[2], pos + len(line)))
            fence = None
        pos += len(line)
    if fence is not None:
        spans.append((fence[2], len(text)))
    for pat in (r"\\\[.*?\\\]", r"\\\(.*?\\\)", r"(?<!`)`[^`\n]+`(?!`)", r"\$\$.*?\$\$"):
        for m in re.finditer(pat, text, flags=re.S):
            spans.append((m.start(), m.end()))
    return sorted(spans)


def _inside(spans, a, b):
    return any(s < b and a < e for s, e in spans)


DEP_LEDGER = re.compile(r"<!--\s*dependency ledger.*?-->", re.S)


def ledger_comment_spans(text: str) -> list:
    return [(m.start(), m.end()) for m in DEP_LEDGER.finditer(text)]


# ---------------------------------------------------------------------------
# Parsing a number list: "1–3", "1, 2 and 4", "4.3 to 4.6"
# ---------------------------------------------------------------------------

def parse_list(s: str, sections: bool):
    """[(item, sep_before)], item an int (chapter) or (chapter, section); sep_before is the
    separator text before the item ('' for the first)."""
    num = SEC_NUM if sections else r"\d+"
    out, pos, sep = [], 0, ""
    for m in re.finditer(num, s):
        sep = s[pos:m.start()]
        tok = m.group(0)
        item = tuple(int(x) for x in tok.split(".")) if sections else int(tok)
        out.append((item, sep))
        pos = m.end()
    return out


def is_range(sep: str) -> bool:
    return bool(re.fullmatch(DASH, sep))


def expand(items):
    """Chapter numbers a parsed chapter list names, ranges expanded."""
    nums = []
    for item, sep in items:
        n = item if isinstance(item, int) else item[0]
        if nums and is_range(sep) and n > nums[-1]:
            nums += list(range(nums[-1] + 1, n + 1))
        else:
            nums.append(n)
    return nums


# ---------------------------------------------------------------------------
# Renumbering
# ---------------------------------------------------------------------------

def _atoms(items):
    """Merge `a<dash>b` into range atoms: [(lo, hi, dash or None, sep_before)]."""
    atoms = []
    for item, sep in items:
        if atoms and is_range(sep):
            lo, _, _, sb = atoms[-1]
            atoms[-1] = (lo, item, sep, sb)
        else:
            atoms.append((item, item, None, sep))
    return atoms


def _chap(item):
    return item if isinstance(item, int) else item[0]


def _map_item(item, mapping):
    """(prefix, local item, atlas id) or None."""
    got = mapping.get(_chap(item))
    if got is None:
        return None
    prefix, n, aid = got
    return prefix, (n if isinstance(item, int) else (n, item[1])), aid


def _fmt(item):
    return str(item) if isinstance(item, int) else f"{item[0]}.{item[1]}"


def _groups(items, mapping):
    """Split a pointer's atoms by volume. Returns [(prefix, [(lo, hi, dash, sep)])] in the
    local numbering, or None if a number is not in the mapping."""
    groups = []
    for lo, hi, dash, sep in _atoms(items):
        if dash is None or isinstance(lo, tuple):   # one item, or a range of sections
            a, b = _map_item(lo, mapping), _map_item(hi, mapping)
            if a is None or b is None:
                return None
            if a[0] != b[0]:
                return None                          # a section range across volumes: leave it
            parts = [(a[0], a[1], b[1] if dash else a[1], dash, sep)]
        else:                                        # a chapter range: split it by volume
            parts = []
            for n in range(lo, hi + 1):
                m = _map_item(n, mapping)
                if m is None:
                    return None
                if parts and parts[-1][0] == m[0] and parts[-1][2] == m[1] - 1:
                    p = parts[-1]
                    parts[-1] = (p[0], p[1], m[1], dash, p[4])
                else:
                    parts.append((m[0], m[1], m[1], dash, sep if not parts else ""))
        for prefix, a, b, d, s in parts:
            atom = (a, b, d if a != b else None, s)
            if groups and groups[-1][0] == prefix and s:
                groups[-1][1].append(atom)
            else:
                groups.append((prefix, [atom]))
    return groups


def _render_atoms(atoms):
    out = []
    for i, (a, b, d, s) in enumerate(atoms):
        piece = _fmt(a) if a == b else f"{_fmt(a)}{d}{_fmt(b)}"
        out.append(piece if i == 0 else f"{s}{piece}")
    return "".join(out)


def _count(atoms):
    return sum(1 if a == b else 2 for a, b, _, _ in atoms)


def _join(pieces, word):
    if len(pieces) == 1:
        return pieces[0]
    if len(pieces) == 2 and not any("," in p for p in pieces):
        return f"{pieces[0]} {word} {pieces[1]}"
    return ", ".join(pieces[:-1]) + f", {word} " + pieces[-1]


def render_prose(kind, items, mapping, here, titles):
    """The pointer `kind items` (old numbers) in the new numbering, read from volume `here`."""
    groups = _groups(items, mapping)
    if groups is None:
        return None
    seps = [s for _, s in items[1:]]
    word = "or" if any(re.search(r"\bor\b", s) for s in seps) else "and"
    base = kind.rstrip("s")
    pieces = []
    for prefix, atoms in groups:
        kw = base + ("s" if _count(atoms) > 1 else "")
        text = f"{kw} {_render_atoms(atoms)}"
        # the volume's own chapters keep their bare number, unless the pointer also names
        # another volume: then every part carries its title
        pieces.append(text if prefix == here and len(groups) == 1 else f"*{titles[prefix]}*, {text}")
    return _join(pieces, word)


def render_atlas(items, mapping):
    """The pointer as atlas ids: `F1.4`, `F1.4 §07`, `F1.3–F2.3`, `F1.1 and F1.2`."""
    out = []
    for i, (item, sep) in enumerate(items):
        got = mapping.get(_chap(item))
        if got is None:
            return None
        aid = got[2]
        tok = aid if isinstance(item, int) else f"{aid} §{item[1]:02d}"
        out.append(tok if i == 0 else f"{sep}{tok}")
    return "".join(out)


def _companion(text, start):
    return bool(COMPANION.search(text[max(0, start - 45):start]))


def rewrite_prose(text, mapping, here, titles, log=None, where=""):
    """Every prose pointer (Chapter/Section) of `text` renumbered for volume `here`.
    Pointers in code and math, and the linear-algebra companion's chapters, are left alone.
    Dependency-ledger comments are rewritten in atlas form (`rewrite_atlas`)."""
    spans = protected_spans(text)
    ledgers = ledger_comment_spans(text)
    edits = []
    for pat, sections in ((CHAPTERS, False), (SECTIONS, True)):
        for m in pat.finditer(text):
            if _inside(spans, m.start(), m.end()) or _inside(ledgers, m.start(), m.end()):
                continue
            if _companion(text, m.start()):
                continue
            items = parse_list(m.group(2), sections)
            if m.group(1).endswith("s") is False and len(items) > 1:
                items = items[:1]          # "Chapter 4 and 5 more": only the first number
                end = m.start(2) + len(str(_fmt(items[0][0])))
            else:
                end = m.end()
            new = render_prose(m.group(1), items, mapping, here, titles)
            if new is None:
                if log is not None:
                    log.append(f"{where}: left as is (not in the map): {m.group(0)!r}")
                continue
            if new != text[m.start():end]:
                edits.append((m.start(), end, new))
                if log is not None:
                    log.append(f"{where}: {text[m.start():end]!r} -> {new!r}")
    for a, b in ledgers:
        seg = text[a:b]
        new = rewrite_atlas(seg, mapping, log, where + " (dependency ledger)")
        if new != seg:
            edits.append((a, b, new))
    return _apply(text, edits)


def rewrite_atlas(text, mapping, log=None, where="", skip_code=True):
    """Every Chapter/Section/Ch N/chNN pointer of `text` as atlas ids (bookkeeping form)."""
    spans = protected_spans(text) if skip_code else []
    edits = []
    taken = []
    for pat, sections in ((SECTIONS, True), (CHAPTERS, False)):
        for m in pat.finditer(text):
            if _inside(spans, m.start(), m.end()) or _inside(taken, m.start(), m.end()):
                continue
            if _companion(text, m.start()):
                continue
            items = parse_list(m.group(2), sections)
            new = render_atlas(items, mapping)
            if new is None:
                if log is not None:
                    log.append(f"{where}: left as is (not in the map): {m.group(0)!r}")
                continue
            edits.append((m.start(), m.end(), new))
            taken.append((m.start(), m.end()))
    for m in CH_ABBR.finditer(text):
        if _inside(spans, m.start(), m.end()) or _inside(taken, m.start(), m.end()):
            continue
        if _companion(text, m.start()):
            continue
        got = mapping.get(int(m.group(1) or m.group(2)))
        if got is None:
            if log is not None:
                log.append(f"{where}: left as is (not in the map): {m.group(0)!r}")
            continue
        edits.append((m.start(), m.end(), got[2]))
    out = _apply(text, edits)
    # "Ch 4 Section 4.9" -> "F1.4 F1.4 §09" -> "F1.4 §09"
    out = re.sub(r"\b([A-Z]{1,3}\d?\.\d+[ab]?) \1 §", r"\1 §", out)
    if log is not None:
        for a, b, new in edits:
            log.append(f"{where}: {text[a:b]!r} -> {new!r}")
    return out


def _apply(text, edits):
    out, last = [], 0
    for a, b, new in sorted(edits):
        if a < last:
            continue
        out += [text[last:a], new]
        last = b
    return "".join(out) + text[last:]


# ---------------------------------------------------------------------------
# References to labels
# ---------------------------------------------------------------------------

REF = re.compile(r"(?<![\w@])@([a-z]+-[\w-]*\w)")
PREFIXED_REF = re.compile(r"@[a-z][a-z0-9]*:(?=[a-z]+-)")


def rewrite_refs(text, owner, here, log=None, where="", skip_code=True):
    """`@label` -> `@prefix:label` where `owner[label]` is another volume's prefix. With
    skip_code=False also inside inline code (a blueprint's `` `@thm-x` ``)."""
    spans = protected_spans(text) if skip_code else []
    edits = []
    for m in REF.finditer(text):
        if _inside(spans, m.start(), m.end()):
            continue
        p = owner.get(m.group(1))
        if p and p != here:
            edits.append((m.start(), m.end(), f"@{p}:{m.group(1)}"))
            if log is not None:
                log.append(f"{where}: @{m.group(1)} -> @{p}:{m.group(1)}")
    return _apply(text, edits)


# ---------------------------------------------------------------------------
# Masking, for hashes
# ---------------------------------------------------------------------------

TOKEN = "‹C›"     # ‹C›
_TITLE = r"(?:\*[^*\n]{1,160}?\*,\s+)?"
_PIECE = (rf"{_TITLE}\b(?:Chapters?|Sections?)\s+(?:\d+(?:\.\d+)?)"
          rf"(?:{SEP_IN}\d+(?:\.\d+)?)*")
_RUN = re.compile(rf"{_PIECE}(?:(?:,\s+|,?\s+and\s+|,?\s+or\s+){_PIECE})*")
_SECT = re.compile(rf"§\s*\d+(?:{DASH}§?\s*\d+)?")
_CHAIN = re.compile(rf"{TOKEN}(?:(?:\s+|\s*,\s*|\s+and\s+|\s+or\s+|{DASH}){TOKEN})+")


def mask(text: str) -> str:
    """`text` with every pointer replaced by one token, and `@prefix:label` read as `@label`."""
    text = PREFIXED_REF.sub("@", text)
    text = _RUN.sub(TOKEN, text)
    text = CH_ABBR.sub(TOKEN, text)
    text = ATLAS_ID.sub(TOKEN, text)
    text = _SECT.sub(TOKEN, text)
    return _CHAIN.sub(TOKEN, text)
