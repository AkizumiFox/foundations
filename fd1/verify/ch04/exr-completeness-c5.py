"""exr-completeness-c5 (Section 4.8, from a closed tree to a derivation): for each search
rule, the sequents the solution uses are derivable. One derivation per case, with the
schematic letters P, Q for phi, psi, checked by tools/check_fitch.py. A two-way case
"Delta, a |- bot and Delta, b |- bot give Delta |- bot" is checked as the sequent
chi, not a, not b |- bot (a list of two formulas a1, a2 as not(a1 and a2)), which is the
same fact by prp-derivable-iff-negation-inconsistent (a); its truth is also checked by table."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L
import _s0708_lib as H

D = {}
D["and"] = r"""\hypo {1} {P \wedge Q}
\have {2} {P} \ae{1}"""
D["not-or"] = r"""\hypo {1} {\neg (P \vee Q)}
\open
\hypo {2} {P}
\have {3} {P \vee Q} \oi{2}
\have {4} {\bot} \ne{3,1}
\close
\have {5} {\neg P} \ni{2-4}"""
D["not-imp-1"] = r"""\hypo {1} {\neg (P \to Q)}
\open
\hypo {2} {\neg P}
\open
\hypo {3} {P}
\have {4} {\bot} \ne{3,2}
\have {5} {Q} \be{4}
\close
\have {6} {P \to Q} \ii{3-5}
\have {7} {\bot} \ne{6,1}
\close
\have {8} {P} \raa{2-7}"""
D["not-imp-2"] = r"""\hypo {1} {\neg (P \to Q)}
\open
\hypo {2} {Q}
\open
\hypo {3} {P}
\have {4} {Q} \r{2}
\close
\have {5} {P \to Q} \ii{3-4}
\have {6} {\bot} \ne{5,1}
\close
\have {7} {\neg Q} \ni{2-6}"""
D["not-not"] = r"""\hypo {1} {\neg \neg P}
\open
\hypo {2} {\neg P}
\have {3} {\bot} \ne{2,1}
\close
\have {4} {P} \raa{2-3}"""
D["or"] = r"""\hypo {1} {P \vee Q}
\hypo {2} {\neg P}
\hypo {3} {\neg Q}
\open
\hypo {4} {P}
\have {5} {\bot} \ne{4,2}
\close
\open
\hypo {6} {Q}
\have {7} {\bot} \ne{6,3}
\close
\have {8} {\bot} \oe{1,4-5,6-7}"""
D["not-and"] = r"""\hypo {1} {\neg (P \wedge Q)}
\hypo {2} {\neg \neg P}
\hypo {3} {\neg \neg Q}
\open
\hypo {4} {\neg P}
\have {5} {\bot} \ne{4,2}
\close
\have {6} {P} \raa{4-5}
\open
\hypo {7} {\neg Q}
\have {8} {\bot} \ne{7,3}
\close
\have {9} {Q} \raa{7-8}
\have {10} {P \wedge Q} \ai{6,9}
\have {11} {\bot} \ne{10,1}"""
D["imp"] = r"""\hypo {1} {P \to Q}
\hypo {2} {\neg \neg P}
\hypo {3} {\neg Q}
\open
\hypo {4} {\neg P}
\have {5} {\bot} \ne{4,2}
\close
\have {6} {P} \raa{4-5}
\have {7} {Q} \ie{1,6}
\have {8} {\bot} \ne{7,3}"""
D["iff"] = r"""\hypo {1} {P \leftrightarrow Q}
\hypo {2} {\neg (P \wedge Q)}
\hypo {3} {\neg (\neg P \wedge \neg Q)}
\have {4} {P \vee \neg P} \lem{}
\open
\hypo {5} {P}
\have {6} {Q} \bie{1,5}
\have {7} {P \wedge Q} \ai{5,6}
\have {8} {\bot} \ne{7,2}
\close
\open
\hypo {9} {\neg P}
\open
\hypo {10} {Q}
\have {11} {P} \bie{1,10}
\have {12} {\bot} \ne{11,9}
\close
\have {13} {\neg Q} \ni{10-12}
\have {14} {\neg P \wedge \neg Q} \ai{9,13}
\have {15} {\bot} \ne{14,3}
\close
\have {16} {\bot} \oe{4,5-8,9-15}"""
D["not-iff"] = r"""\hypo {1} {\neg (P \leftrightarrow Q)}
\hypo {2} {\neg (P \wedge \neg Q)}
\hypo {3} {\neg (\neg P \wedge Q)}
\have {4} {P \vee \neg P} \lem{}
\open
\hypo {5} {P}
\open
\hypo {6} {Q}
\open
\hypo {7} {P}
\have {8} {Q} \r{6}
\close
\open
\hypo {9} {Q}
\have {10} {P} \r{5}
\close
\have {11} {P \leftrightarrow Q} \bi{7-8,9-10}
\have {12} {\bot} \ne{11,1}
\close
\have {13} {\neg Q} \ni{6-12}
\have {14} {P \wedge \neg Q} \ai{5,13}
\have {15} {\bot} \ne{14,2}
\close
\open
\hypo {16} {\neg P}
\open
\hypo {17} {\neg Q}
\open
\hypo {18} {P}
\have {19} {\bot} \ne{18,16}
\have {20} {Q} \be{19}
\close
\open
\hypo {21} {Q}
\have {22} {\bot} \ne{21,17}
\have {23} {P} \be{22}
\close
\have {24} {P \leftrightarrow Q} \bi{18-20,21-23}
\have {25} {\bot} \ne{24,1}
\close
\have {26} {Q} \raa{17-25}
\have {27} {\neg P \wedge Q} \ai{16,26}
\have {28} {\bot} \ne{27,3}
\close
\have {29} {\bot} \oe{4,5-15,16-28}"""
text = "\n\n".join("```{=latex}\n$\\begin{nd}\n" + b + "\n\\end{nd}$\n```" for b in D.values())
H.check(text, derivations=len(D))
# truth of the two-way sequents, by table (lowercase copies)
for prem in ([r"p \vee q", r"\neg p", r"\neg q"], [r"\neg(p \wedge q)", r"\neg\neg p", r"\neg\neg q"],
             [r"p \to q", r"\neg\neg p", r"\neg q"], [r"p \leftrightarrow q", r"\neg(p \wedge q)", r"\neg(\neg p \wedge \neg q)"],
             [r"\neg(p \leftrightarrow q)", r"\neg(p \wedge \neg q)", r"\neg(\neg p \wedge q)"]):
    assert not L.entails(prem, r"\bot")
# RAA appears in the cases the solution names, LEM in the two biconditional cases
raa = sorted(k for k, b in D.items() if "\\raa" in b)
assert raa == sorted(["not-imp-1", "not-not", "not-and", "imp", "not-iff"]), raa
assert sorted(k for k, b in D.items() if "\\lem" in b) == ["iff", "not-iff"]
print("exr-completeness-c5: all quoted values check")
