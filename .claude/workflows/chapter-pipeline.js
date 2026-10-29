export const meta = {
  name: 'chapter-pipeline',
  description: 'Run one chapter through PIPELINE.md stages S2-S8: blueprint check, parallel drafting, referees A/B + exercise verifier, revision, fresh re-check, seam review',
  whenToUse: 'Produce one chapter of the analysis book end to end from its hand-written blueprint',
  phases: [
    { title: 'Blueprint', detail: 'S2 re-verification of the blueprint against the current book' },
    { title: 'Draft', detail: 'S3 section groups drafted in parallel' },
    { title: 'Review', detail: 'S5 referee A, referee B, S6 exercise verifier (independent)' },
    { title: 'Revise', detail: 'S7 revision and fresh re-check (up to 2 rounds)' },
    { title: 'Seam', detail: 'S8 seam review' },
  ],
}

const A = args
const NN = String(A.num).padStart(2, '0')
const REPO = '~/coding/analysis-book'
const DIR = `src/ch${NN}-${A.slug}`
const SCRATCH = '/tmp/claude-1000/-home-akizumi-coding-analysis/8d99e54f-c6f3-4bed-98e0-b546ef5dc565/scratchpad'
const BP = `authoring/blueprints/ch${NN}.md`
const COMMON = `You work in ${REPO} (the analysis textbook). Chapter ${A.num}: "${A.title}" (slug ${A.slug}, directory ${DIR}/, binding blueprint ${BP}, sidecars verify/ch${NN}/, ledger authoring/ledger/ch${NN}.yaml). Stage briefs are in authoring/PIPELINE.md; writing rules in authoring/STYLE.md (all, incl. §10–§11), NOTATION.md, DRAFTING.md. Python tools needing yaml run with .venv/bin/python. Never build in the shared tree: copy it with rsync (exclude .venv and _build) into your own scratch directory under ${SCRATCH}/ named after your stage, and build there. Other agents may be editing other chapters concurrently; touch only what your stage allows. ${A.extra || ''}`

const REVIEW = {
  type: 'object',
  properties: {
    counts: { type: 'object', properties: { correct: { type: 'integer' }, minor: { type: 'integer' }, gap: { type: 'integer' }, error: { type: 'integer' } }, required: ['correct', 'minor', 'gap', 'error'] },
    serious: { type: 'array', items: { type: 'string' }, description: 'every gap and error, one line each with location' },
    reportFile: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['counts', 'serious', 'reportFile'],
}
const RECHECK = {
  type: 'object',
  properties: {
    accepted: { type: 'integer' }, rejected: { type: 'integer' },
    rejectedItems: { type: 'array', items: { type: 'string' } },
    reportFile: { type: 'string' },
  },
  required: ['accepted', 'rejected', 'rejectedItems', 'reportFile'],
}

phase('Blueprint')
const s2 = A.reviewOnly ? null : await agent(`${COMMON}
Stage S2a (blueprint statement referee) for ${BP}. It was written and S2-reviewed earlier, but the book has since changed (the logic chapters were split: Chapter 1 connectives-and-derivations, Chapter 2 negation-and-classical-logic; their blueprints ch01.md/ch02.md and any drafted text in src/ch01-*/ src/ch02-* are the truth for labels and rules). Re-verify adversarially per the S2 brief: every statement, proof route, intended exercise answer and marking scheme; every label the blueprint cites from earlier chapters exists (in src or in an earlier chapter's hand-written blueprint) with the meaning assumed; derivations claimed (write them in a scratch .md, run python3 tools/check_fitch.py); closeness to the reference books (blueprint/sources.yaml; Huth & Ryan especially: ~/math-refs/analysis/converted/00 Logic & Proofs/Huth & Ryan - Logic in Computer Science (2nd ed)/sections/). Write authoring/reviews/ch${NN}-S2-recheck.md and APPLY confident edits to ${BP}. Run .venv/bin/python blueprint/check_blueprint.py ${A.num} to 0 problems. Touch only ${BP} and the review file.`, { label: `S2 ch${NN}`, schema: REVIEW })
log(`S2: ${JSON.stringify(s2 && s2.counts)}`)

phase('Draft')
const drafts = A.reviewOnly ? [] : await parallel((A.groups || []).map((g, i) => () => agent(`${COMMON}
Stage S3 drafting, following authoring/DRAFTING.md exactly. Write these files of ${DIR}/: ${g.files.join(', ')}. Other agents write the chapter's other files in parallel (${A.groups.filter((_, j) => j !== i).map(x => x.files.join(', ')).join(' | ')}): use exactly the blueprint's labels; cite later-section labels only where the blueprint allows (never in proofs). ${A.direction || ''}
Gates before you finish: python3 tools/check_fitch.py ${DIR}; python3 tools/check_structure.py; python3 tools/check_numbers.py (sidecars verify/ch${NN}/<label>.py for every computation or explicit constant); build html and pdf in your scratch copy ${SCRATCH}/ch${NN}-draft-${i + 1}/repo and LOOK at rendered derivations/formulas; .venv/bin/python blueprint/originality.py ${A.num}. Unresolved refs to sections other agents are writing are expected. End each section with its dependency-ledger comment. Write final files into ${REPO}/${DIR}/. Your final answer: files written, word counts, labels created, deviations from the blueprint and why, promises opened, claims you are unsure about.`, { label: `S3 ch${NN} ${g.label}`, phase: 'Draft' })))

phase('Review')
const [refA, refB, ver] = await parallel([
  () => agent(`${COMMON}
Stage S5a, Referee A (proofs) — follow your brief in PIPELINE.md. Read-only on src. Chapter ${DIR}/ against ${BP}. Check every proof and derivation line by line (rerun python3 tools/check_fitch.py; hand-check blocks marked % schema or % expect-invalid), every chosen constant and its stated dependence, every hypothesis used, a counterexample attempt per theorem with a dropped hypothesis, every meta-argument, every 'needs/does not need' claim. Write authoring/reviews/ch${NN}-S5-A.md (table: file:line, item, verdict correct/minor/gap/error, evidence). Do NOT write the ledger (the reviser records verdicts).`, { label: `S5a ch${NN}`, phase: 'Review', schema: REVIEW }),
  () => agent(`${COMMON}
Stage S5b, Referee B (claims and bookkeeping) — follow your brief in PIPELINE.md; read BOTTOM-UP. Read-only on src. Check every prose meta-claim (about this chapter, earlier chapters' text, later chapters' blueprints), cross-section consistency, dependency ledgers vs actual use, promises (python3 tools/promises.py --for ${A.num}, --reconcile), forward deps (python3 tools/check_forward_deps.py), STYLE compliance (python3 tools/check_structure.py), notation (python3 tools/check_notation.py), and rendered output (build in ${SCRATCH}/ch${NN}-refB/repo; python3 tools/check_rendered.py; look at pages). Write authoring/reviews/ch${NN}-S5-B.md (table). Do NOT write the ledger.`, { label: `S5b ch${NN}`, phase: 'Review', schema: REVIEW }),
  () => agent(`${COMMON}
Stage S6, exercise and solution verifier — follow your brief in PIPELINE.md. Read-only on src. For every B, C, R exercise and exit check: solve it yourself BEFORE reading the book's solution (derivations in scratch .md files under ${SCRATCH}/ch${NN}-S6/, checked with python3 tools/check_fitch.py; numbers checked in python), then compare: correct, complete, all parts, fair marking scheme, hints not giving the key step, find-the-error items flawed exactly where stated, every B-type task has a worked example in its section. Run python3 tools/check_numbers.py. Write authoring/reviews/ch${NN}-S6.md (table). Do NOT write the ledger.`, { label: `S6 ch${NN}`, phase: 'Review', schema: REVIEW }),
])
log(`Review: A ${JSON.stringify(refA && refA.counts)} | B ${JSON.stringify(refB && refB.counts)} | S6 ${JSON.stringify(ver && ver.counts)}`)

phase('Revise')
let recheck = null
let round = 0
let extra = ''
while (round < 2) {
  round++
  await agent(`${COMMON}
Stage S7, reviser (round ${round}). Fix every finding (error, gap, minor) in authoring/reviews/ch${NN}-S5-A.md, ch${NN}-S5-B.md, ch${NN}-S6.md${round > 1 ? ` and the REJECTED items in authoring/reviews/ch${NN}-S7-recheck.md` : ''}, minimally and in the chapter's voice; fix overlapping findings once; you may dispute a finding with a stated reason. Initialise the ledger if missing (.venv/bin/python tools/ledger.py init ${A.num}) and record each review's verdicts and your resolution (stages S5a/S5b/S6 with --by refereeA/refereeB/verifier as the reviews state, then S7 --by reviser). Reconcile authoring/STATUS.md's promise table (python3 tools/promises.py --reconcile). Append a Resolution section to each review file. Verify in ${SCRATCH}/ch${NN}-S7r${round}/repo: build html, pdf, check; python3 -m pytest tests -q; check_fitch, check_structure, check_numbers, check_rendered; originality. Write fixes into ${REPO} (${DIR}/, verify/ch${NN}/, STATUS.md, NOTATION.md, reviews, ledger). Final answer: each finding → fix, disputes with reasons.${extra}`, { label: `S7 ch${NN} r${round}`, phase: 'Revise' })
  recheck = await agent(`${COMMON}
Stage S7 acceptance: you are a FRESH re-referee who has not seen this chapter. Read the reviews authoring/reviews/ch${NN}-S5-A.md, ch${NN}-S5-B.md, ch${NN}-S6.md with their Resolution sections, and the uncommitted diff (git -C ${REPO} diff -- ${DIR} verify/ch${NN} authoring/STATUS.md authoring/NOTATION.md). For each finding: fixed correctly / fixed with a new problem / not fixed; check every changed sentence is true in context, edited derivations pass check_fitch, changed exercises stay correct and fair, nothing else changed unintentionally. Write authoring/reviews/ch${NN}-S7-recheck.md (round ${round}) and record verdicts in the ledger (stage S7r, --by rereferee). Read-only on src.`, { label: `S7r ch${NN} r${round}`, phase: 'Revise', schema: RECHECK })
  log(`Re-check round ${round}: accepted ${recheck && recheck.accepted}, rejected ${recheck && recheck.rejected}`)
  if (!recheck || recheck.rejected === 0) break
  extra = ` Previously rejected: ${recheck.rejectedItems.join(' | ')}`
}

phase('Seam')
const seam = await agent(`${COMMON}
Stage S8, seam referee — follow your brief in PIPELINE.md. Check the chapter as a whole: index.md vs sections; cross-section consistency; promises opened/paid (python3 tools/promises.py --for ${A.num}, --reconcile; STATUS.md); seams with earlier chapters (every cited label exists and means what is assumed — src and hand-written blueprints) and with later chapters' blueprints (labels and claims they plan to cite from this chapter); python3 tools/check_notation.py, check_structure. Write authoring/reviews/ch${NN}-S8-seam.md and record ledger verdicts (stage S8, --by seam). You MAY fix minor issues directly in ${DIR}/ (typesetting, wording, @ref conversions, ledger comments), in STATUS.md and NOTATION.md, re-running check_fitch/check_structure and a build in ${SCRATCH}/ch${NN}-S8/repo afterwards; list anything larger instead of fixing it.`, { label: `S8 ch${NN}`, phase: 'Seam', schema: REVIEW })

return { chapter: A.num, s2: s2 && s2.counts, drafts: drafts.map(d => (d || '').slice(0, 1500)), refA: refA && refA.counts, refB: refB && refB.counts, s6: ver && ver.counts, recheckRounds: round, lastRecheck: recheck, seam }
