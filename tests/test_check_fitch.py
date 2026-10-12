"""Tests for tools/check_fitch.py: Fitch derivations and truth tables, checked by machine."""

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "check_fitch.py"
spec = importlib.util.spec_from_file_location("check_fitch", TOOL)
fitch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fitch)


def block(body, marker=False, options=""):
    """A raw LaTeX block around one nd; marker True means expect-invalid, or a marker name."""
    if marker is True:
        marker = "expect-invalid"
    head = ("```{=latex}\n" + (f"% {marker} (a comment)\n" if marker else "")
            + "\\begin{center}\n$\\begin{nd}" + options + "\n")
    return "Some prose.\n\n" + head + body.strip("\n") + "\n\\end{nd}$\n\\end{center}\n```\n"


def errors(body, marker=False):
    e, _, _ = fitch.check_text(block(body, marker))
    return [m for _, m in e]


TRANSITIVE = r"""
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
"""


class FormulaTests(unittest.TestCase):
    def test_precedence_and_macros(self):
        f = fitch.parse_formula(r"\neg P \wedge Q \to R \vee {\bot}")
        self.assertEqual(f, ("imp", ("and", ("not", ("var", "P")), ("var", "Q")),
                             ("or", ("var", "R"), ("bot",))))

    def test_leftrightarrow_is_not_eaten_by_left(self):
        self.assertEqual(fitch.parse_formula(r"P \leftrightarrow Q")[0], "iff")

    def test_non_propositional_text_is_rejected(self):
        for text in (r"x > 2", r"\quad \vdots", r"\forall x P(x)"):   # first-order: parse_fo
            with self.assertRaises(fitch.ParseError):
                fitch.parse_formula(text)


class DerivationTests(unittest.TestCase):
    def test_valid_derivation_is_clean(self):
        self.assertEqual(errors(TRANSITIVE), [])

    def test_all_propositional_rules_accepted(self):
        body = r"""
  \hypo {1} {P \wedge (Q \vee R)}
  \hypo {2} {P \leftrightarrow S}
  \have {3} {P} \ae{1}
  \have {4} {Q \vee R} \ae{1}
  \have {5} {S} \bie{2,3}
  \open
  \hypo {6} {Q}
  \have {7} {S \wedge Q} \ai{5,6}
  \have {8} {(S \wedge Q) \vee R} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {(S \wedge Q) \vee R} \oi{9}
  \close
  \have {11} {(S \wedge Q) \vee R} \oe{4,6-8,9-10}
  \open
  \hypo {12} {\neg P}
  \have {13} {\bot} \ne{3,12}
  \have {14} {\bot} \r{13}
  \close
  \have {15} {\neg\neg P} \ni{12-14}
  \open
  \hypo {16} {\neg S}
  \have {17} {\bot} \ne{5,16}
  \close
  \have {18} {S} \raa{16-17}
  \have {19} {S} \r{18}
"""
        self.assertEqual(errors(body), [])
        ex_falso = r"\hypo {1} {P} \hypo {2} {\neg P} \have {3} {\bot} \ne{1,2} \have {4} {Q} \be{3}"
        self.assertEqual(errors(ex_falso), [])
        self.assertTrue(errors(ex_falso.replace(r"\be{3}", r"\be{1}")))

    def test_and_intro_cites_its_lines_in_either_order(self):
        """STYLE §12 / NOTATION: the written line decides which conjunct is which."""
        base = "\\hypo {1} {P} \\hypo {2} {Q} "
        for cite in ("1,2", "2,1"):
            for line in ("P \\wedge Q", "Q \\wedge P"):
                self.assertEqual(errors(base + f"\\have {{3}} {{{line}}} \\ai{{{cite}}}"), [], (cite, line))
        self.assertTrue(errors(base + "\\have {3} {P \\wedge P} \\ai{1,2}"))      # not those lines
        self.assertTrue(errors(base + "\\have {3} {P \\vee Q} \\ai{2,1}"))        # not a conjunction
        # ->E is read the same whichever line is cited first (the implication-first order is
        # a writing convention, not a rule the checker enforces)
        imp = "\\hypo {1} {P \\to Q} \\hypo {2} {P} "
        self.assertEqual(errors(imp + "\\have {3} {Q} \\ie{1,2}"), [])
        self.assertEqual(errors(imp + "\\have {3} {Q} \\ie{2,1}"), [])

    def test_citing_inside_a_closed_box(self):
        body = TRANSITIVE + r"  \have {7} {R} \r{5}" + "\n"
        self.assertEqual(errors(body), ["line 7 cites line 5, inside a box that has closed"])

    def test_citing_a_later_line_and_a_missing_line(self):
        body = r"""
  \hypo {1} {P}
  \have {2} {P \wedge P} \ai{1,3}
  \have {3} {P} \r{1}
  \have {4} {P} \r{9}
"""
        msgs = errors(body)
        self.assertIn("line 2 cites line 3, a later line", msgs)
        self.assertIn("line 4 cites line 9, which does not exist", msgs)

    def test_range_must_be_a_closed_box(self):
        body = r"""
  \hypo {1} {P}
  \hypo {2} {Q}
  \have {3} {P \to Q} \ii{1-2}
"""
        self.assertTrue(any("not a box" in m for m in errors(body)))

    def test_citing_an_open_box(self):
        body = r"""
  \open
  \hypo {1} {P}
  \have {2} {P \to P} \ii{1-1}
  \close
"""
        self.assertTrue(any("still open" in m for m in errors(body)))

    def test_wrong_rule_shapes(self):
        body = r"""
  \hypo {1} {P \to Q}
  \hypo {2} {Q}
  \have {3} {P} \ie{1,2}
  \open
  \hypo {4} {P}
  \have {5} {\bot} \by{assumed}{}
  \close
  \have {6} {P} \raa{4-5}
  \have {7} {P \wedge Q} \ae{1}
"""
        msgs = errors(body)
        self.assertTrue(any(m.startswith("line 3: →E") for m in msgs), msgs)
        self.assertTrue(any(m.startswith("line 6: RAA") for m in msgs), msgs)
        self.assertTrue(any(m.startswith("line 7: ∧E") for m in msgs), msgs)

    def test_duplicate_labels_and_bad_box(self):
        body = r"""
  \hypo {1} {P}
  \open
  \have {2} {P} \r{1}
  \close
  \have {2} {P} \r{1}
"""
        msgs = errors(body)
        self.assertIn("line label 2 used twice", msgs)
        self.assertTrue(any("does not begin with an assumption" in m for m in msgs))

    def test_wrong_number_of_citations(self):
        self.assertTrue(any("cites a line, a line" in m for m in
                            errors(r"\hypo {1} {P} \have {2} {P \wedge P} \ai{1}")))

    def test_unmarked_schematic_labels_are_an_error(self):
        body = r"""
  \open
  \hypo {i} {\neg P}
  \have {} {\quad \vdots}
  \have {j} {\bot}
  \close
  \have {k} {P} \raa{i-j}
"""
        msgs = errors(body)
        self.assertEqual(len(msgs), 1)
        self.assertIn("non-numeric line labels", msgs[0])
        e, notes, counts = fitch.check_text(block(body, marker="schema"))
        self.assertEqual((e, counts["schema"]), ([], 1))

    def test_vdots_are_notes(self):
        body2 = r"""
  \have {1} {P \vee \neg P} \by{excluded middle}{}
  \open
  \hypo {2} {\neg P}
  \have[\ ][0] {} {\quad \vdots}
  \have[][3] {3} {\bot}
  \close
  \have {4} {P} \raa{2-3}
"""
        e, notes, _ = fitch.check_text(block(body2))
        self.assertEqual(e, [])
        # without the optional arguments fitch.sty numbers the \vdots row itself
        plain = body2.replace(r"\have[\ ][0]", r"\have").replace(r"\have[][3]", r"\have")
        self.assertIn("line label 3 prints as 4", errors(plain))
        self.assertTrue(any("follows \\vdots" in m for _, m in notes))
        self.assertTrue(any("justified by text" in m for _, m in notes))

    def test_expect_invalid(self):
        bad = TRANSITIVE + r"  \have {7} {R} \r{5}" + "\n"
        e, notes, counts = fitch.check_text(block(bad, marker=True))
        self.assertEqual(e, [])
        self.assertEqual(counts["expected_invalid"], 1)
        e, _, _ = fitch.check_text(block(TRANSITIVE, marker=True))
        self.assertEqual([m for _, m in e], ["marked % expect-invalid but checks clean"])


RAA_SCHEMA = r"""
  \open
  \hypo[i][0] {i} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {\bot}
  \close
  \have[k][0] {k} {P} \raa{i-j}
  \have {k1} {P \vee Q} \oi{k}
"""


def schema_result(body, options=""):
    e, notes, counts = fitch.check_text(block(body, marker="schema", options=options))
    return [m for _, m in e], [m for _, m in notes], counts


class OptionalArgumentTests(unittest.TestCase):
    def test_printed_numbers(self):
        lines, _, errs = fitch.parse_nd(r"""
  \hypo {1} {P}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {Q}
  \have[n][-1] {a} {Q}
  \have {b} {Q}
  \have[m] {c} {Q}
  \have {d} {Q}
""", 1)
        self.assertEqual(errs, [])
        self.assertEqual([ln.display for ln in lines], ["1", "\\ ", "7", "n-1", "n", "m", "m+1"])
        self.assertEqual([ln.label for ln in lines], ["1", "", "7", "a", "b", "c", "d"])
        self.assertTrue(lines[1].gap and not lines[2].gap)

    def test_guards_and_open_options_are_skipped(self):
        lines, boxes, errs = fitch.parse_nd(r"\open[x] \hypo {1}[x] {P} \close", 1)
        self.assertEqual((errs, len(boxes), lines[0].text), ([], 1, "P"))

    def test_schema_key_prints_labels(self):
        lines, _, _ = fitch.parse_nd(r"\hypo {i} {P} \have {j} {P} \r{i}", 1, schema_key=True)
        self.assertEqual([ln.display for ln in lines], ["i", "j"])

    def test_stray_number_after_blank_base(self):
        msgs = errors(r"""
  \hypo {1} {P}
  \have[\ ][0] {} {\vdots}
  \have {7} {P} \r{1}
""")
        self.assertTrue(any("stray number +1" in m for m in msgs), msgs)

    def test_jump_only_across_a_gap(self):
        partial = r"""
  \hypo {1} {P \to \neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {P}
  \have {8} {P \wedge (P \to \neg Q)} \ai{7,1}
"""
        self.assertEqual(schema_result(partial)[0], [])
        no_gap = r"""
  \hypo {1} {P}
  \have[][7] {7} {P} \r{1}
"""
        self.assertTrue(any("not numbered 1, 2, 3" in m for m in errors(no_gap)))
        mismatch = r"""
  \hypo {1} {P}
  \have[\ ][0] {} {\vdots}
  \have[][7] {6} {P}
"""
        self.assertIn("line label 6 prints as 7", schema_result(mismatch)[0])


class SchemaTests(unittest.TestCase):
    def test_schema_is_clean_and_counted(self):
        msgs, notes, counts = schema_result(RAA_SCHEMA)
        self.assertEqual(msgs, [])
        self.assertEqual((counts["schema"], counts["expected_invalid"]), (1, 0))
        self.assertTrue(any("follows \\vdots" in m for m in notes))

    def test_nd_schema_option_implies_schema(self):
        body = RAA_SCHEMA.replace("[i][0] ", "").replace("[j][0] ", "").replace("[k][0] ", "") \
                         .replace(r"\have[\ ][0]", r"\have")
        e, _, counts = fitch.check_text(block(body, options="[schema]"))
        self.assertEqual((e, counts["schema"]), ([], 1))

    def test_rule_shapes_still_checked(self):
        msgs, _, _ = schema_result(RAA_SCHEMA.replace(r"{P} \raa", r"{\neg P} \raa"))
        self.assertTrue(any(m.startswith("line k: RAA") for m in msgs), msgs)
        msgs, _, _ = schema_result(RAA_SCHEMA.replace(r"{P \vee Q}", r"{Q \wedge P}"))
        self.assertTrue(any(m.startswith("line k1: ∨I") for m in msgs), msgs)

    def test_scope_still_checked(self):
        msgs, _, _ = schema_result(RAA_SCHEMA + r"  \have {k2} {\bot} \r{j}" + "\n")
        self.assertIn("line k2 cites line j, inside a box that has closed", msgs)
        msgs, _, _ = schema_result(RAA_SCHEMA.replace(r"\raa{i-j}", r"\raa{i-z}"))
        self.assertTrue(any("does not exist" in m for m in msgs), msgs)
        msgs, _, _ = schema_result(RAA_SCHEMA.replace(r"\close", "").replace(r"\raa{i-j}", r"\raa{i-j}"))
        self.assertTrue(msgs)                       # unclosed box

    def test_given_lines_gaps_and_metavariables_are_notes(self):
        body = r"""
  \have[i][0] {i} {\varphi}
  \have[j][0] {j} {P}
  \have[k][0] {k} {\varphi \wedge P} \ai{i,j}
  \open
  \hypo[l][0] {l} {Q}
  \close
  \have[m][0] {m} {Q} \oe{}
"""
        msgs, notes, _ = schema_result(body)
        self.assertEqual(msgs, [])
        self.assertTrue(any("line i unjustified" in m for m in notes), notes)
        self.assertTrue(any("line k: formula of line k not propositional" in m for m in notes), notes)
        self.assertTrue(any("line m cites nothing yet" in m for m in notes), notes)
        self.assertTrue(errors(body.replace(r"\have[i][0] {i} {\varphi}", r"\hypo {1} {P}")))

    def test_markers_are_per_nd_and_nearest_wins(self):
        text = ("```{=latex}\n% schema (outer comment)\n\\begin{center}\n% schema\n$\\begin{nd}\n"
                + RAA_SCHEMA + "\\end{nd}$\n\\qquad\n% expect-invalid\n$\\begin{nd}\n"
                + TRANSITIVE + "  \\have {7} {R} \\r{5}\n\\end{nd}$\n\\qquad\n$\\begin{nd}\n"
                + TRANSITIVE + "\\end{nd}$\n\\end{center}\n```\n")
        e, _, counts = fitch.check_text(text)
        self.assertEqual((e, counts["schema"], counts["expected_invalid"]), ([], 1, 1))
        starts = [m.start() for m in fitch.ND.finditer(text)]
        self.assertEqual([fitch.block_marker(text, s) for s in starts],
                         ["schema", "expect-invalid", None])


class FirstOrderFormulaTests(unittest.TestCase):
    def test_terms_predicates_and_binders(self):
        f = fitch.parse_fo(r"\forall x\, P(x) \to \exists y\, R(f(x), y_0)")
        self.assertEqual(f, ("imp", ("forall", "x", ("pred", "P", (("v", "x"),)), None),
                             ("exists", "y", ("pred", "R", (("app", "f", (("v", "x"),)),
                                                             ("v", "y_0"))), None)))
        self.assertEqual(fitch.parse_fo(r"x_{0} \ne 0"),
                         ("not", ("rel", "=", ("v", "x_0"), ("v", "0"))))
        b = fitch.parse_fo(r"\forall \varepsilon > 0\, \exists N \forall n \ge N\, \abs{a_n - L} < \varepsilon")
        self.assertEqual((b[0], b[1], b[3]), ("forall", r"\varepsilon",
                                              ("rel", ">", ("v", r"\varepsilon"), ("v", "0"))))
        self.assertEqual(fitch.parse_fo(r"(a + b)^2 \ge 0")[0], "rel")
        self.assertEqual(fitch.read_formula(r"P \wedge Q"), ("and", ("var", "P"), ("var", "Q")))

    def test_metavariables_and_prose_are_rejected(self):
        for text in (r"\forall x\, \varphi", r"\varphi[t/x]", r"p \text{ even}", r"a < b < c"):
            with self.assertRaises(fitch.ParseError):
                fitch.parse_fo(text)

    def test_substitution_and_free_for(self):
        phi = fitch.parse_fo(r"\exists y\, (y > x) \wedge P(x)")
        t = fitch.parse_fo(r"y + 1 = 0")[2]            # the term y + 1
        self.assertEqual(fitch.subst(phi, "x", ("v", "c")),
                         fitch.parse_fo(r"\exists y\, (y > c) \wedge P(c)"))
        self.assertFalse(fitch.free_for(t, "x", phi))
        self.assertTrue(fitch.free_for(t, "x", fitch.parse_fo(r"\forall z\, (x < z)")))
        self.assertEqual(fitch.subst(fitch.parse_fo(r"\forall x\, P(x)"), "x", ("v", "c")),
                         fitch.parse_fo(r"\forall x\, P(x)"))


def has(msgs, *parts):
    return any(all(p in m for p in parts) for m in msgs)


class UniversalEliminationTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(errors(r"""
  \hypo {1} {\forall x (P(x) \to P(f(x)))}
  \hypo {2} {P(c)}
  \have {3} {P(c) \to P(f(c))} \Ae{1}
  \have {4} {P(f(c))} \ie{3,2}
  \have {5} {P(f(c)) \to P(f(f(c)))} \Ae{1}
  \have {6} {P(f(f(c)))} \ie{5,4}
"""), [])

    def test_capture(self):
        msgs = errors(r"""
  \hypo {1} {\forall x \exists y\, (y \ne x)}
  \have {2} {\exists y\, (y \ne y)} \Ae{1}
""")
        self.assertTrue(has(msgs, "line 2: ∀E", "not free for x"), msgs)

    def test_not_an_instance(self):
        partial = errors(r"\hypo {1} {\forall x\, R(x, x)} \have {2} {R(c, d)} \Ae{1}")
        self.assertTrue(has(partial, "line 2: ∀E", "instance"), partial)
        buried = errors(r"\hypo {1} {\forall x\, P(x) \to Q} \have {2} {P(c) \to Q} \Ae{1}")
        self.assertTrue(has(buried, "line 2: ∀E", "no ∀ line"), buried)


class UniversalIntroductionTests(unittest.TestCase):
    NESTED = r"""
  \hypo {1} {\forall x \forall y\, R(x, y)}
  \open[y_0]
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have {3} {R(x_0, y_0)} \Ae{2}
  \close
  \have {4} {\forall x\, R(x, y_0)} \Ai{2-3}
  \close
  \have {5} {\forall y \forall x\, R(x, y)} \Ai{2-4}
"""

    def test_flagged_box_without_assumption(self):
        self.assertEqual(errors(r"""
  \hypo {1} {\forall x \forall y\, R(x, y)}
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have {3} {R(x_0, x_0)} \Ae{2}
  \close
  \have {4} {\forall x\, R(x, x)} \Ai{2-3}
"""), [])
        self.assertEqual(errors(self.NESTED), [])

    def test_unflagged_box(self):
        msgs = errors(r"""
  \hypo {1} {\forall x\, P(x)}
  \open
  \have {2} {P(x_0)} \Ae{1}
  \close
  \have {3} {\forall x\, P(x)} \Ai{2-2}
""")
        self.assertTrue(has(msgs, "does not begin with an assumption"), msgs)
        self.assertTrue(has(msgs, "line 3: ∀I", "flagged box"), msgs)

    def test_wrong_last_line_and_assumption(self):
        msgs = errors(r"""
  \hypo {1} {\forall x\, P(x)}
  \open[x_0]
  \have {2} {P(x_0)} \Ae{1}
  \close
  \have {3} {\forall x\, Q(x)} \Ai{2-2}
""")
        self.assertTrue(has(msgs, "line 3: ∀I", "ending in Q(x_0)"), msgs)
        msgs = errors(r"""
  \open[x_0]
  \hypo {1} {P(x_0)}
  \close
  \have {2} {\forall x\, P(x)} \Ai{1-1}
""")
        self.assertTrue(has(msgs, "line 2: ∀I", "no assumption"), msgs)

    def test_name_in_premise(self):
        msgs = errors(r"""
  \hypo {1} {P(x_0)}
  \open[x_0]
  \have {2} {P(x_0)} \r{1}
  \close
  \have {3} {\forall x\, P(x)} \Ai{2-2}
""")
        self.assertTrue(has(msgs, "line 3: ∀I", "x_0 occurs in the premise 1"), msgs)

    def test_name_in_open_assumption(self):
        msgs = errors(r"""
  \open
  \hypo {1} {x_0 > 0}
  \open[x_0]
  \have {2} {x_0 > 0} \r{1}
  \close
  \have {3} {\forall x\, (x > 0)} \Ai{2-2}
  \close
  \have {4} {x_0 > 0 \to \forall x\, (x > 0)} \ii{1-3}
""")
        self.assertTrue(has(msgs, "line 3: ∀I", "open assumption 1"), msgs)
        self.assertEqual(len(msgs), 1, msgs)

    def test_name_in_conclusion(self):
        msgs = errors(r"""
  \hypo {1} {\forall x \forall y\, R(x, y)}
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have {3} {R(x_0, x_0)} \Ae{2}
  \close
  \have {4} {\forall x\, R(x, x_0)} \Ai{2-3}
""")
        self.assertTrue(has(msgs, "line 4: ∀I", "occurs in the conclusion"), msgs)

    def test_last_line_inside_an_inner_box(self):
        msgs = errors(r"""
  \hypo {1} {\forall x\, P(x)}
  \open[x_0]
  \open
  \hypo {2} {Q}
  \have {3} {P(x_0)} \Ae{1}
  \close
  \close
  \have {4} {\forall x\, P(x)} \Ai{2-3}
""")
        self.assertTrue(has(msgs, "line 4: ∀I", "a line of the box itself"), msgs)


class ExistentialIntroductionTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(errors(r"""
  \hypo {1} {R(c, c)}
  \have {2} {\exists x\, R(x, c)} \Ei{1}
  \have {3} {\exists x\, R(c, x)} \Ei{1}
  \have {4} {\exists x\, R(x, x)} \Ei{1}
  \have {5} {\exists y\, (P(y) \vee \exists x\, R(x, x))} \by{not this rule}{}
"""), [])
        self.assertEqual(errors(r"""
  \hypo {1} {\forall x\, P(x)}
  \have {2} {P(x)} \Ae{1}
  \have {3} {\exists x\, P(x)} \Ei{2}
"""), [])

    def test_capture(self):
        msgs = errors(r"\hypo {1} {\forall y\, R(y, y)} \have {2} {\exists x \forall y\, R(x, y)} \Ei{1}")
        self.assertTrue(has(msgs, "line 2: ∃I", "not free for x"), msgs)

    def test_not_an_instance(self):
        msgs = errors(r"\hypo {1} {\exists x\, R(x, x)} \have {2} {\exists x\, R(x, c)} \Ei{1}")
        self.assertTrue(has(msgs, "line 2: ∃I", "instance"), msgs)


EXISTS_AND = r"""
  \hypo {1} {\exists x (P(x) \wedge Q(x))}
  \open[x_0]
  \hypo {2} {P(x_0) \wedge Q(x_0)}
  \have {3} {P(x_0)} \ae{2}
  \have {4} {\exists x\, P(x)} \Ei{3}
  \have {5} {Q(x_0)} \ae{2}
  \have {6} {\exists x\, Q(x)} \Ei{5}
  \have {7} {\exists x\, P(x) \wedge \exists x\, Q(x)} \ai{4,6}
  \close
  \have {8} {\exists x\, P(x) \wedge \exists x\, Q(x)} \Ee{1,2-7}
"""


class ExistentialEliminationTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(errors(EXISTS_AND), [])
        guard_on_hypo = EXISTS_AND.replace(r"\open[x_0]", r"\open").replace(r"\hypo {2}", r"\hypo {2}[x_0]")
        self.assertEqual(errors(guard_on_hypo), [])
        self.assertEqual(errors(r"""
  \hypo {1} {\exists x\, P(x)}
  \hypo {2} {\forall x (P(x) \to \neg Q(x))}
  \open
  \hypo {3} {\forall x\, Q(x)}
  \open[x_0]
  \hypo {4} {P(x_0)}
  \have {5} {P(x_0) \to \neg Q(x_0)} \Ae{2}
  \have {6} {\neg Q(x_0)} \ie{5,4}
  \have {7} {Q(x_0)} \Ae{3}
  \have {8} {\bot} \ne{7,6}
  \close
  \have {9} {\bot} \Ee{1,4-8}
  \close
  \have {10} {\neg \forall x\, Q(x)} \ni{3-9}
"""), [])

    def test_unflagged_box_and_wrong_assumption(self):
        msgs = errors(EXISTS_AND.replace(r"\open[x_0]", r"\open"))
        self.assertTrue(has(msgs, "line 8: ∃E", "flagged box"), msgs)
        msgs = errors(r"""
  \hypo {1} {\exists x\, P(x)}
  \open[x_0]
  \hypo {2} {Q(x_0)}
  \have {3} {\exists x\, Q(x)} \Ei{2}
  \close
  \have {4} {\exists x\, Q(x)} \Ee{1,2-3}
""")
        self.assertTrue(has(msgs, "line 4: ∃E", "must assume P(x_0)"), msgs)

    def test_name_in_conclusion(self):
        msgs = errors(r"""
  \hypo {1} {\exists x (P(x) \wedge Q(x))}
  \open[x_0]
  \hypo {2} {P(x_0) \wedge Q(x_0)}
  \have {3} {P(x_0)} \ae{2}
  \close
  \have {4} {P(x_0)} \Ee{1,2-3}
  \have {5} {\exists x\, P(x)} \Ei{4}
""")
        self.assertEqual(len(msgs), 1, msgs)
        self.assertTrue(has(msgs, "line 4: ∃E", "occurs in the conclusion"), msgs)

    def test_name_in_the_exists_line(self):
        msgs = errors(r"""
  \hypo {1} {\forall y \exists x\, R(x, y)}
  \have {2} {\exists x\, R(x, x_0)} \Ae{1}
  \open[x_0]
  \hypo {3} {R(x_0, x_0)}
  \have {4} {\exists z\, R(z, z)} \Ei{3}
  \close
  \have {5} {\exists z\, R(z, z)} \Ee{2,3-4}
""")
        self.assertEqual(len(msgs), 1, msgs)
        self.assertTrue(has(msgs, "line 5: ∃E", "occurs in the ∃ line"), msgs)

    WITH_Q = r"""
  \hypo {1} {\exists x\, P(x)}
  %s
  \open[x_0]
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \wedge Q(x_0)} \ai{3,2}
  \have {5} {\exists x (P(x) \wedge Q(x))} \Ei{4}
  \close
  \have {6} {\exists x (P(x) \wedge Q(x))} \Ee{1,3-5}
"""

    def test_name_in_premise(self):
        msgs = errors(self.WITH_Q % r"\hypo {2} {Q(x_0)}")
        self.assertEqual(len(msgs), 1, msgs)
        self.assertTrue(has(msgs, "line 6: ∃E", "x_0 occurs in the premise 2"), msgs)

    def test_name_in_open_assumption(self):
        body = (self.WITH_Q % "\\open\n  \\hypo {2} {Q(x_0)}") + \
            "  \\close\n  \\have {7} {Q(x_0) \\to \\exists x (P(x) \\wedge Q(x))} \\ii{2-6}\n"
        msgs = errors(body)
        self.assertEqual(len(msgs), 1, msgs)
        self.assertTrue(has(msgs, "line 6: ∃E", "open assumption 2"), msgs)


class EqualityTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(errors(r"""
  \hypo {1} {a = b}
  \have {2} {a = a} \eqi{}
  \have {3} {b = a} \eqe{1,2}
  \have {4} {f(a) = f(a)} \eqi{}
  \have {5} {f(a) = f(b)} \eqe{1,4}
  \have {6} {a + a = 2a} \by{arith}{}
  \have {7} {b + a = 2a} \eqe{1,6}
  \have {8} {b + b = 2b} \eqe{1,6}
"""), [])

    def test_reflexivity_shape(self):
        msgs = errors(r"\have {1} {a = b} \eqi{}")
        self.assertTrue(has(msgs, "line 1: =I"), msgs)

    def test_wrong_direction_and_no_equation(self):
        msgs = errors(r"\hypo {1} {a = b} \hypo {2} {P(b)} \have {3} {P(a)} \eqe{1,2}")
        self.assertTrue(has(msgs, "line 3: =E", "needs an equation"), msgs)
        msgs = errors(r"\hypo {1} {a < b} \hypo {2} {P(a)} \have {3} {P(b)} \eqe{1,2}")
        self.assertTrue(has(msgs, "line 3: =E", "no equation"), msgs)

    def test_capture(self):
        msgs = errors(r"""
  \hypo {1} {x = 0}
  \hypo {2} {\forall x\, (x = x)}
  \have {3} {\forall x\, (0 = x)} \eqe{1,2}
""")
        self.assertTrue(has(msgs, "line 3: =E", "not free for x"), msgs)


class BoundedQuantifierTests(unittest.TestCase):
    def test_bounded_rules(self):
        self.assertEqual(errors(r"""
  \hypo {1} {\forall x \in A\, P(x)}
  \hypo {2} {c \in A}
  \have {3} {P(c)} \Ae{1,2}
  \have {4} {\exists x \in A\, P(x)} \Ei{2,3}
  \open[x_0]
  \hypo {5} {x_0 \in A}
  \have {6} {P(x_0)} \Ae{1,5}
  \have {7} {P(x_0) \vee Q(x_0)} \oi{6}
  \close
  \have {8} {\forall x \in A\, (P(x) \vee Q(x))} \Ai{5-7}
  \open[y_0]
  \hypo {9} {y_0 \in A}
  \hypo {10} {P(y_0)}
  \have {11} {\exists y\, P(y)} \Ei{10}
  \close
  \have {12} {\exists y\, P(y)} \Ee{4,9-11}
"""), [])

    def test_bound_must_match(self):
        msgs = errors(r"""
  \hypo {1} {\forall x \in A\, P(x)}
  \hypo {2} {c \in B}
  \have {3} {P(c)} \Ae{1,2}
""")
        self.assertTrue(has(msgs, "line 3: ∀E"), msgs)


class QuantifierSchemaTests(unittest.TestCase):
    def test_blueprint_schemas_are_clean_with_notes(self):
        schemas = [r"""
  \have {i} {\forall x\, \varphi}
  \have {k} {\varphi[t/x]} \Ae{i}
""", r"""
  \open[x_0]
  \have {i} {\vdots}
  \have {j} {\varphi[x_0/x]}
  \close
  \have {k} {\forall x\, \varphi} \Ai{i-j}
""", r"""
  \have {h} {\exists x\, \varphi}
  \open[x_0]
  \hypo {i} {\varphi[x_0/x]}
  \have {} {\vdots}
  \have {j} {\chi}
  \close
  \have {k} {\chi} \Ee{h,i-j}
""", r"""
  \have {k} {t = t} \eqi{}
""", r"""
  \have {i} {t_1 = t_2}
  \have {j} {\varphi[t_1/x]}
  \have {k} {\varphi[t_2/x]} \eqe{i,j}
"""]
        for body in schemas:
            e, notes, _ = fitch.check_text(block(body, options="[schema]"))
            self.assertEqual(e, [], body)
        self.assertTrue(any("not propositional or first-order" in m for m in
                            schema_result(schemas[0])[1]))


class TruthTableTests(unittest.TestCase):
    TABLE = r"""
\[
\begin{array}{cc|cc}
P & Q & P \to Q & \neg P \vee Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & %s
\end{array}
\]
"""

    def test_correct_table(self):
        e, _, counts = fitch.check_text(self.TABLE % r"\mathrm{T}")
        self.assertEqual((e, counts["tables"]), ([], 1))

    def test_wrong_entry(self):
        e, _, _ = fitch.check_text(self.TABLE % r"\mathrm{F}")
        self.assertEqual(len(e), 1)
        self.assertIn("row 4", e[0][1])

    def test_non_truth_table_array_ignored(self):
        e, _, counts = fitch.check_text(r"\[ \begin{array}{cc} 1 & 2 \\ \hline 3 & 4 \end{array} \]")
        self.assertEqual((e, counts["tables"]), ([], 0))


class PurposeTests(unittest.TestCase):
    r"""\purpose{\ii} on an assumption: why it is made, checked against the rule that
    closes its box."""

    def test_matching_purpose_is_clean(self):
        body = TRANSITIVE.replace(r"\hypo {3} {P}", r"\hypo {3} {P} \purpose{\ii}")
        self.assertEqual(errors(body), [])

    def test_wrong_purpose_is_an_error(self):
        body = TRANSITIVE.replace(r"\hypo {3} {P}", r"\hypo {3} {P} \purpose{\ni}")
        e = errors(body)
        self.assertEqual(len(e), 1)
        self.assertIn("made for ¬I, but its box is closed by →I (line 6)", e[0])

    def test_every_box_of_or_elimination(self):
        body = r"""
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P} \purpose{\oe}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q} \purpose{\raa}
  \have {5} {Q \vee P} \oi{4}
  \close
  \have {6} {Q \vee P} \oe{1,2-3,4-5}
"""
        e = errors(body)
        self.assertEqual(len(e), 1)
        self.assertIn("assumption 4 is made for RAA, but its box is closed by ∨E", e[0])

    def test_flagged_existential_box(self):
        body = r"""
  \hypo {1} {\exists x P(x)}
  \open
  \hypo {2}[x_0] {P(x_0)} \purpose{\Ee}
  \have {3} {\exists y P(y)} \Ei{2}
  \close
  \have {4} {\exists y P(y)} \Ee{1,2-3}
"""
        self.assertEqual(errors(body), [])

    def test_purpose_on_a_premise_or_a_derived_line(self):
        e = errors(TRANSITIVE.replace(r"\hypo {1} {P \to Q}", r"\hypo {1} {P \to Q} \purpose{\ii}"))
        self.assertTrue(any("premise 1 has a \\purpose" in m for m in e), e)
        e = errors(TRANSITIVE.replace(r"\have {4} {Q} \ie{1,3}", r"\have {4} {Q} \purpose{\ii}"))
        self.assertTrue(any("line 4 has a \\purpose" in m for m in e), e)

    def test_purpose_naming_no_box_rule(self):
        for arg in (r"\ie", "for implication"):
            e = errors(TRANSITIVE.replace(r"\hypo {3} {P}", r"\hypo {3} {P} \purpose{%s}" % arg))
            self.assertEqual(len(e), 1, e)
            self.assertIn("names no rule that closes a box", e[0])

    def test_unclosed_box_is_a_note(self):
        body = r"""
  \hypo {1} {P}
  \open
  \hypo {2} {Q} \purpose{\ii}
  \have {3} {P} \r{1}
  \close
"""
        e, notes, _ = fitch.check_text(block(body))
        self.assertEqual(e, [])
        self.assertTrue(any("not cited by a later line" in m for _, m in notes))

    def test_inferred_purposes_are_listed(self):
        found = []
        fitch.check_text(block(TRANSITIVE.replace(r"\hypo {3} {P}", r"\hypo {3} {P} \purpose{\ii}")),
                         purposes=found)
        self.assertEqual([item[1:] for item in found], [("3", "ii", "ii")])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "a.md"
            path.write_text(block(TRANSITIVE))
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(fitch.main([str(path), "--purposes"]), 0)
            self.assertIn("assumption 3: for →I", out.getvalue())


class TautTests(unittest.TestCase):
    r"""\by{TAUT}{refs} (or \taut{refs}): a truth-functional step, checked by a truth
    table over the propositional skeleton (atomic and quantified subformulas are letters)."""

    def taut(self, premises, line, refs=None, macro=r"\by{TAUT}"):
        rows = [r"  \hypo {%d} {%s}" % (n, f) for n, f in enumerate(premises, 1)]
        n = len(premises) + 1
        refs = ",".join(str(k) for k in range(1, n)) if refs is None else refs
        rows.append(r"  \have {%d} {%s} %s{%s}" % (n, line, macro, refs))
        return errors("\n".join(rows))

    def test_propositional_consequence(self):
        self.assertEqual(self.taut([r"P \to Q", r"\neg Q"], r"\neg P"), [])
        self.assertEqual(self.taut([r"\neg (P \wedge Q)"], r"\neg P \vee \neg Q", macro=r"\taut"), [])

    def test_tautology_with_no_lines(self):
        self.assertEqual(self.taut([], r"P \vee \neg P", refs=""), [])
        e = self.taut([], r"P \vee Q", refs="")
        self.assertEqual(len(e), 1)
        self.assertIn("is not a tautology", e[0])

    def test_non_consequence_names_a_row(self):
        e = self.taut([r"P \to Q", "Q"], "P")
        self.assertEqual(len(e), 1)
        self.assertIn("TAUT does not follow truth-functionally", e[0])
        self.assertIn("P F", e[0])

    def test_quantified_subformulas_are_letters(self):
        self.assertEqual(self.taut([r"\forall x P(x) \to \exists y Q(y)", r"\neg \exists y Q(y)"],
                                   r"\neg \forall x P(x)"), [])
        # alike up to bound names: one letter
        self.assertEqual(self.taut([r"\neg \neg \forall x P(x)"], r"\forall z P(z)"), [])
        self.assertEqual(self.taut([r"\exists x (P(x) \wedge Q(x)) \wedge x = 0"],
                                   r"x = 0 \wedge \exists y (P(y) \wedge Q(y))"), [])

    def test_first_order_validity_is_no_taut_step(self):
        # C2: swapping quantifiers is valid, but not truth-functional
        e = self.taut([r"\forall x \forall y R(x, y)"], r"\forall y \forall x R(x, y)")
        self.assertEqual(len(e), 1)
        self.assertIn("does not follow truth-functionally", e[0])
        e = self.taut([r"\forall x P(x)"], r"P(c)")
        self.assertEqual(len(e), 1)

    def test_free_variables_tell_letters_apart(self):
        e = self.taut([r"P(x) \vee \neg P(x)", r"\neg P(y)"], r"\neg P(x)")
        self.assertEqual(len(e), 1)

    def test_taut_cannot_cite_a_box(self):
        body = r"""
  \open
  \hypo {1} {P}
  \have {2} {P} \r{1}
  \close
  \have {3} {P \to P} \by{TAUT}{1-2}
"""
        e = errors(body)
        self.assertTrue(any("TAUT cites lines, not a box" in m for m in e), e)

    def test_other_by_text_is_still_skipped(self):
        e, notes, _ = fitch.check_text(block(r"""
  \hypo {1} {P}
  \have {2} {Q} \by{Def}{1}
"""))
        self.assertEqual(e, [])
        self.assertTrue(any("justified by text (Def)" in m for _, m in notes))


class CliTests(unittest.TestCase):
    def test_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "good.md"
            good.write_text(block(TRANSITIVE))
            bad = Path(tmp) / "bad.md"
            bad.write_text(block(TRANSITIVE + r"  \have {7} {R} \r{5}" + "\n"))
            with redirect_stdout(io.StringIO()):
                self.assertEqual(fitch.main([str(good)]), 0)
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(fitch.main([str(bad)]), 1)
            self.assertIn("bad.md", out.getvalue())


if __name__ == "__main__":
    unittest.main()
