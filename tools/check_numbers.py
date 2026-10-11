#!/usr/bin/env python3
"""Run the numeric sidecars in `verify/` and check that the text quotes what they check.

`authoring/DRAFTING.md` asks for a sidecar script `verify/chNN/<label>.py` for every
non-trivial computation and every chosen constant: it puts the values the text quotes
in a dict `QUOTED = {...}` at the top, asserts each one from an independent
computation, and exits non-zero on failure. This tool (research-production §6) does
three things with them:

* fatal    -- **run** every sidecar (`verify/chNN/*.py`, except helpers whose name
  starts with `_`) from the repo root, with `.venv/bin/python` when it exists; a
  non-zero exit, or a run over `--timeout` seconds, is a failure;
* fatal    -- **cross-check** the QUOTED dict against the source: the sidecar is named
  after a label, the label's `{#label}` is found in `src/` (by grep, falling back to
  `_build/crossref_labels.json`), and every value in QUOTED must appear literally in
  that section file. A sidecar whose label is nowhere in `src/` is also fatal.
* advisory -- **missing sidecars**: a labelled block (with the solution that follows
  it) that contains a decimal number, a numeric fraction, or an explicit constant
  (`N = 12`, `\\varepsilon \\coloneqq \\frac1{10}`) and has no sidecar of its own name;
  and a sidecar with no QUOTED dict, or with a value this tool cannot read.

What "appears literally" means, per value type in QUOTED (read with `ast`, never
executed; `Fraction(p, q)`/`F(p, q)`/`Rational(p, q)` calls are understood):

* an integer: the digits, not inside a longer number, with a minus sign (`-`, `−`)
  in front if it is negative; thousands may be grouped (`2{,}047`, `2,047`);
* a fraction p/q: `\\frac{p}{q}` (also `\\tfrac`, `\\dfrac`, `\\frac12`, `\\frac1{10}`),
  `p/q`, or its decimal expansion when that terminates (`3/2` as `1.5`);
* a float: its decimal form;
* a string: the string itself, ignoring whitespace;
* a tuple, list, set or dict value: each element, separately;
* `True`, `False`, `None`: nothing to look for (they record that a claim holds).

The keys of QUOTED are descriptions for the reader of the script and are not checked.

    python3 tools/check_numbers.py                  # every chapter under verify/
    python3 tools/check_numbers.py 11               # only verify/ch11
    python3 tools/check_numbers.py --no-run         # cross-check only, do not run
    python3 tools/check_numbers.py --advisory       # also list blocks with no sidecar

Exits 1 if any fatal problem is found. Importable:

    from tools.check_numbers import find_violations, report
    fatal, advisory = find_violations(Path("verify"), Path("src"))

In a series, run it in a volume directory or pass `--book fd2` (chapter numbers are the
volume's own; sidecars run from the volume directory). As a `./build.py check` plugin
(config `checks`, with `"requires": "verify"`), `run(book, labels)` runs every sidecar.
"""
import argparse
import ast
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import series  # noqa: E402

VERIFY = Path("verify")
SRC = Path("src")
CROSSREF = Path("_build/crossref_labels.json")
TIMEOUT = 120
LABEL_DEF = re.compile(r"\{#([a-z]+-[\w-]+)")
FRACTION_CALLS = {"F", "Fraction", "Rational", "R", "Q"}


class Unreadable(Exception):
    pass


# ---------------------------------------------------------------------------
# Sidecars
# ---------------------------------------------------------------------------

def sidecars(verify: Path, chapters=None) -> list:
    """Every sidecar script under `verify/chNN/`, optionally only for `chapters`."""
    out = []
    for d in sorted(Path(verify).glob("ch[0-9]*")):
        m = re.match(r"ch(\d+)", d.name)
        if not d.is_dir() or (chapters and int(m.group(1)) not in chapters):
            continue
        out += [f for f in sorted(d.glob("*.py")) if not f.name.startswith("_")]
    return out


def default_python(root: Path) -> str:
    """The book's virtualenv, or the repository's (a volume's parent), or this interpreter."""
    for base in (Path(root), Path(root).resolve().parent):
        venv = base / ".venv" / "bin" / "python"
        if venv.exists():
            return str(venv)
    return sys.executable


def run_sidecar(path: Path, python: str, root: Path, timeout: int = TIMEOUT):
    """(ok, last lines of output)."""
    try:
        r = subprocess.run([python, str(Path(path).resolve())], cwd=root, capture_output=True,
                           text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, f"timed out after {timeout}s"
    out = (r.stdout + r.stderr).strip().splitlines()
    return r.returncode == 0, " / ".join(out[-3:]) if out else f"exit {r.returncode}"


def _value(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        v = _value(node.operand)
        if isinstance(v, (int, float, Fraction)) and not isinstance(v, bool):
            return -v if isinstance(node.op, ast.USub) else v
        raise Unreadable(ast.unparse(node))
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        return tuple(_value(e) for e in node.elts)
    if isinstance(node, ast.Dict):
        return tuple(_value(v) for v in node.values)
    if isinstance(node, ast.Call):
        name = node.func.id if isinstance(node.func, ast.Name) else \
            node.func.attr if isinstance(node.func, ast.Attribute) else ""
        if name in FRACTION_CALLS and 1 <= len(node.args) <= 2 and not node.keywords:
            args = [_value(a) for a in node.args]
            if all(isinstance(a, (int, str)) and not isinstance(a, bool) for a in args):
                return Fraction(*args)
    raise Unreadable(ast.unparse(node))


def load_quoted(path: Path):
    """The QUOTED dict of a sidecar as {key: value}, read without running it.

    Returns None if the script has no top-level `QUOTED = {...}`. A value that is not a
    literal (or a Fraction call) becomes an `Unreadable` instance.
    """
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(t, ast.Name) and t.id == "QUOTED" for t in targets) \
                    and isinstance(node.value, ast.Dict):
                out = {}
                for k, v in zip(node.value.keys, node.value.values):
                    key = k.value if isinstance(k, ast.Constant) else ast.unparse(k)
                    try:
                        out[key] = _value(v)
                    except Unreadable as e:
                        out[key] = e
                return out
    return None


# ---------------------------------------------------------------------------
# Literal forms of a value
# ---------------------------------------------------------------------------

MINUS = r"(?:-|−|\\text\{-\}|\{-\})\s*"


def _int_re(n: int) -> str:
    digits = str(abs(n))
    grouped = [digits]
    if len(digits) > 3:
        parts = []
        s = digits
        while s:
            parts.insert(0, s[-3:])
            s = s[:-3]
        grouped += [sep.join(parts) for sep in ("{,}", ",", r"\,", " ")]
    body = "(?:" + "|".join(re.escape(g) for g in grouped) + ")"
    sign = MINUS if n < 0 else ""
    lead = "" if sign else r"(?<!frac)(?<!frac\d)"      # not the digits of \frac12
    return rf"(?<![\d.]){lead}{sign}{body}(?![\d]|\.\d)"


def _frac_re(p: int, q: int) -> list:
    def arg(k):
        s = str(k)
        return rf"(?:\{{\s*{s}\s*\}}|{s})" if len(s) == 1 else rf"\{{\s*{s}\s*\}}"
    sign = MINUS if p < 0 else ""
    a = abs(p)
    forms = [rf"{sign}\\[dt]?frac\s*{arg(a)}\s*{arg(q)}",
             rf"\\[dt]?frac\s*\{{\s*-\s*{a}\s*\}}\s*{arg(q)}" if p < 0 else None,
             rf"(?<![\d.]){sign}{a}\s*/\s*{q}(?!\d)"]
    d = q
    for f in (2, 5):
        while d % f == 0:
            d //= f
    if d == 1:                       # terminating decimal
        forms.append(_dec_re(abs(Fraction(p, q)), negative=p < 0))
    return [f for f in forms if f]


def _dec_re(x, negative=False) -> str:
    """Regex for a decimal expansion of x >= 0 (a terminating Fraction or a float)."""
    if isinstance(x, Fraction):
        k = 0
        while (x * 10**k).denominator != 1:
            k += 1
        n = int(x * 10**k)
        s = str(n).rjust(k + 1, "0")
        text = s[:-k] + "." + s[-k:] if k else s
    else:
        text = repr(float(x))
        if text.endswith(".0"):
            text = text[:-2]
    whole, _, frac = text.partition(".")
    pat = re.escape(whole) + (r"(?:\.|\{\.\}|\{,\})" + re.escape(frac) if frac else "")
    if whole == "0" and frac:
        pat = "0?" + pat              # .5 for 0.5
    return rf"(?<![\d.]){MINUS if negative else ''}{pat}(?![\d])"


def forms(value) -> list:
    """(description, regex or None) for each atom of a QUOTED value.

    None as the regex means there is nothing to look for (a bool or None).
    """
    if isinstance(value, tuple):
        return [f for v in value for f in forms(v)]
    if isinstance(value, bool) or value is None:
        return [(repr(value), None)]
    if isinstance(value, int):
        return [(str(value), _int_re(value))]
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return [(str(value.numerator), _int_re(value.numerator))]
        return [(f"{value.numerator}/{value.denominator}",
                 "|".join(f"(?:{r})" for r in _frac_re(value.numerator, value.denominator)))]
    if isinstance(value, float):
        if value == int(value):
            return [(repr(value), _int_re(int(value)))]
        return [(repr(value), _dec_re(abs(value), negative=value < 0))]
    if isinstance(value, str):
        return [(repr(value), "STR:" + re.sub(r"\s+", "", value))]
    return [(repr(value), None)]


def appears(regex: str, text: str, squashed: str) -> bool:
    if regex.startswith("STR:"):
        return regex[4:] in squashed
    return re.search(regex, text) is not None


# ---------------------------------------------------------------------------
# Labels -> source files
# ---------------------------------------------------------------------------

def label_files(src: Path, crossref: Path = CROSSREF) -> dict:
    """{label: section file} from a grep of `{#label` in src, then the crossref registry."""
    out = {}
    for f in sorted(Path(src).rglob("*.md")):
        for label in LABEL_DEF.findall(f.read_text(encoding="utf-8")):
            out.setdefault(label, f)
    crossref = Path(crossref)
    if crossref.exists():
        try:
            data = json.loads(crossref.read_text(encoding="utf-8"))
            data = data.get("crossref_labels", data)
            for label, info in data.items():
                if label in out or not isinstance(info, dict) or not info.get("file"):
                    continue
                cand = Path(src) / Path(info["file"]).with_suffix(".md")
                if cand.exists():
                    out[label] = cand
        except (ValueError, OSError):
            pass
    return out


# ---------------------------------------------------------------------------
# Blocks that look like they need a sidecar
# ---------------------------------------------------------------------------

NOISE = [
    re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.S),
    re.compile(r"\b(?:Sections?|Chapters?|Theorems?|Examples?|Exercises?|Definitions?|"
               r"Lemmas?|Corollary|Propositions?|Figures?)\s+\d+(?:\.\d+)*"),
    re.compile(r"§\s*\d+(?:\.\d+)*"),
    re.compile(r"\{[^{}]*options=\"[^\"]*\"[^{}]*\}"),
    re.compile(r"\\(?:hspace|vspace|kern|hskip|raisebox|scalebox|rule)\*?\{[^}]*\}"),
    re.compile(r"-?\d*\.?\d+\s*(?:em|ex|pt|cm|mm|in)\b"),
]
DECIMAL = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])")
NUM_FRAC = re.compile(r"\\[dt]?frac\s*(?:\{\s*-?\d+\s*\}|\d)\s*(?:\{\s*\d+\s*\}|\d)")
CONSTANT = re.compile(
    r"(?:\\(?:varepsilon|epsilon|delta|eta)|(?<![\\\w])[A-Za-z](?:_\{?\w+\}?)?)"
    r"\s*(?:=|\\coloneqq)\s*-?\s*"
    r"(?:\d+\.\d+|\d{2,}|[2-9]|\\[dt]?frac\s*(?:\{\s*\d+\s*\}|\d)\s*(?:\{\s*\d+\s*\}|\d))"
    r"(?![\w.])")


def numeric_reason(text: str):
    """Why a block looks like it quotes numbers, or None."""
    for rx in NOISE:
        text = rx.sub(" ", text)
    for rx, why in ((DECIMAL, "decimal"), (NUM_FRAC, "fraction"), (CONSTANT, "constant")):
        m = rx.search(text)
        if m:
            return f"{why} `{m.group(0).strip()}`"
    return None


def numeric_blocks(chapter_dir: Path) -> list:
    """(file, lineno, label, reason) for each top-level labelled block that quotes numbers."""
    out = []
    for f in sorted(Path(chapter_dir).glob("[0-9]*.md")):
        doc = mdblocks.parse(f.read_text(encoding="utf-8"))
        lines = ["" if code else ln for ln, code in zip(doc.lines, doc.in_code)]
        for div in doc.top:
            if not div.id or "-" not in div.id:
                continue
            end = div.end
            nxt = mdblocks.following_div(doc, div)
            while nxt is not None and nxt.has("solution"):
                end = nxt.end
                nxt = mdblocks.following_div(doc, nxt)
            why = numeric_reason("\n".join(lines[div.start:end + 1]))
            if why:
                out.append((f, div.start + 1, div.id, why))
    return out


# ---------------------------------------------------------------------------
# The check
# ---------------------------------------------------------------------------

def find_violations(verify: Path = VERIFY, src: Path = SRC, chapters=None, run: bool = True,
                    python: str | None = None, root: Path = Path("."), crossref: Path = CROSSREF,
                    timeout: int = TIMEOUT):
    """Returns (fatal, advisory): lists of (path, lineno, message)."""
    root = Path(root)
    python = python or default_python(root)
    fatal, advisory = [], []
    where = label_files(src, crossref)
    scripts = sidecars(verify, chapters)
    for s in scripts:
        if run:
            ok, out = run_sidecar(s, python, root, timeout)
            if not ok:
                fatal.append((s, 0, f"sidecar fails: {out}"))
        label = s.stem
        try:
            quoted = load_quoted(s)
        except SyntaxError as e:
            fatal.append((s, e.lineno or 0, f"cannot parse: {e.msg}"))
            continue
        if quoted is None:
            advisory.append((s, 0, "no QUOTED dict"))
        target = where.get(label)
        if target is None:
            fatal.append((s, 0, f"no block {{#{label}}} in {src}"))
            continue
        if not quoted:
            continue
        text = target.read_text(encoding="utf-8")
        squashed = re.sub(r"\s+", "", text)
        for key, value in quoted.items():
            if isinstance(value, Unreadable):
                advisory.append((s, 0, f"QUOTED[{key!r}] is not a literal ({value}); not cross-checked"))
                continue
            for desc, rx in forms(value):
                if rx is not None and not appears(rx, text, squashed):
                    fatal.append((s, 0, f"QUOTED[{key!r}] = {desc} does not appear in "
                                        f"{_rel(target, root)}"))
    have = {(s.parent.name, s.stem) for s in scripts} | \
           {(s.parent.name, s.stem) for s in sidecars(verify)}
    for chdir in sorted(Path(src).glob("ch[0-9]*")):
        m = re.match(r"ch(\d+)", chdir.name)
        if not chdir.is_dir() or (chapters and int(m.group(1)) not in chapters):
            continue
        vname = f"ch{int(m.group(1)):02d}"
        for f, ln, label, why in numeric_blocks(chdir):
            if (vname, label) not in have:
                advisory.append((f, ln, f"{label}: {why}, but no {verify}/{vname}/{label}.py"))
    return fatal, advisory


def _rel(path: Path, root: Path):
    try:
        return Path(path).resolve().relative_to(Path(root).resolve())
    except ValueError:
        return path


def report(items) -> str:
    return "\n".join(f"{p}:{ln}: {m}" if ln else f"{p}: {m}" for p, ln, m in items)


def main(argv=None) -> int:
    argv = series.enter_book(argv)
    ap = argparse.ArgumentParser(
        description="Run the verify/chNN sidecars and check their QUOTED values appear in the source.")
    series.add_book_arg(ap)
    ap.add_argument("chapters", nargs="*", type=int, help="chapter numbers (default: all)")
    ap.add_argument("--verify", default=str(VERIFY), help="sidecar directory (default: verify)")
    ap.add_argument("--src", default=str(SRC), help="source directory (default: src)")
    ap.add_argument("--python", help="interpreter for the sidecars (default: .venv/bin/python if present)")
    ap.add_argument("--no-run", action="store_true", help="do not run the sidecars; cross-check only")
    ap.add_argument("--advisory", action="store_true",
                    help="list the advisories (blocks with numbers but no sidecar, ...)")
    ap.add_argument("--timeout", type=int, default=TIMEOUT, help=f"seconds per sidecar (default {TIMEOUT})")
    args = ap.parse_args(argv)
    fatal, advisory = find_violations(Path(args.verify), Path(args.src), set(args.chapters) or None,
                                      run=not args.no_run, python=args.python, timeout=args.timeout)
    n = len(sidecars(Path(args.verify), set(args.chapters) or None))
    if advisory and args.advisory:
        print("Advisory:")
        print(report(advisory))
        print()
    if fatal:
        print("Fatal:")
        print(report(fatal))
    print(f"\n{n} sidecar(s){'' if args.no_run else ' run'}: {len(fatal)} fatal, "
          f"{len(advisory)} advisory{'' if args.advisory else ' (--advisory to list)'}.")
    return 1 if fatal else 0


def run(book, labels):
    """The engine's check plugin protocol (build/plugins.py): (errors, warnings)."""
    root = Path(book.root)
    fatal, advisory = find_violations(root / "verify", book.src_dir, root=root,
                                      crossref=book.build_dir / "crossref_labels.json")
    errors = report([(Path(p).resolve().relative_to(root.resolve()), n, m)
                     for p, n, m in fatal]).splitlines()
    warnings = ([f"{len(advisory)} numeric-sidecar advisory note(s); run "
                 f"`python3 tools/check_numbers.py --book {root.name} --advisory` to list them"]
                if advisory else [])
    return errors, warnings

if __name__ == "__main__":
    sys.exit(main())
