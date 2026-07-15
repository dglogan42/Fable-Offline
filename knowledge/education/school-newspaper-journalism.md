# Student journalist kit — school newspaper craft seed

**Skill:** `student-journalist-kit`
**Related:** `highschool-play-scripter` (school-safe content-mode pattern) · `book-creator-comics-kit` (print layout) · `google-for-education` (editorial workflow)
**Not legal advice.** Student press law varies by school/country; school policy and faculty advisor decisions always outrank this file's defaults.

---

## Why this exists

School newspapers run into the same failure mode as any publisher: an unverified claim about a real, identifiable person gets printed as fact and causes real harm (to the subject) and real risk (to the paper/school). This skill exists to put a **source-verification gate** in front of anything that could read as an accusation, before it ever reaches layout — the same discipline used anywhere a claim about a real person or business is about to be published.

---

## Ethics core (universal, school-adapted)

| Principle | School-paper application |
|---|---|
| Accuracy | Every fact and quote traceable to a real, checkable source |
| Fairness | Subject of a critical piece gets a chance to respond before publish |
| Independence | Advertisers, clubs, or staff pressure don't dictate coverage |
| Accountability | Visible corrections, not silent edits |
| Minimise harm | Extra care naming/photographing minors; weigh newsworthiness against harm |

---

## NZ context (VERIFY LIVE / school policy governs)

| Topic | Note |
|---|---|
| Defamation | Defamation Act 2013 — an unattributed claim of wrongdoing against a real person is a legal risk, not just an ethics one |
| Privacy of minors | Privacy Act 2020 — naming/photographing students, especially on sensitive topics, typically needs consent per school policy |
| School policy | Most schools have their own student-press or media policy; where it conflicts with this file, the school policy wins |

---

## Content-mode gate

| Mode | Use for | Requires |
|------|---------|----------|
| **G** | Events, clubs, sports recaps, lighthearted features | Normal editing |
| **T** | Investigative pieces, policy editorials, sensitive topics | Named on-record sources, advisor sign-off, right-of-reply offered to any subject of criticism |

If a pitch includes an accusation against a real person/business with no attributed source: **stop, ask for the source, do not draft** — softening the language ("some say...", "allegedly...") is not a substitute for a real source.

---

## Newsroom structure (seed scaffold)

```text
workspace/education/student-journalist/
  edition-plan.md      # section list, deadlines, print/web
  pitches.md            # story-pitch entries
  drafts/                # in-progress articles by slug
  fact-check-log.md     # source verification per piece naming a real person
  corrections.md        # visible correction log
```

---

## Story shapes

| Shape | Structure |
|---|---|
| News | Inverted pyramid: lede → nut graf → body (importance order) → attribution throughout |
| Editorial | Labeled opinion; position early; named evidence; acknowledges strongest counter-argument; critiques policy/conduct, not private character |
| Feature | Scene-setting lede → subject's own real words → context/stakes → closing image |

---

## Quick style defaults

| Rule | Default |
|---|---|
| Numbers | Spell out one–nine, numerals 10+ |
| Titles | Full name + role on first reference, last name after |
| Quotes | Exact words only; `[bracket]` any clarifying edit |
| Attribution verb | "said" over embellished alternatives |

---

## Related Fable skills

| Skill | Overlap |
|---|---|
| `highschool-play-scripter` | Same G/T content-mode shape, applied to stage scripts instead of news |
| `book-creator-comics-kit` | Print-page panel/layout conventions if the edition is illustrated |
| `google-for-education` | Docs/Classroom-based editorial workflow |
| `rss-share` | Web edition feed |
| `calendar-mail-meetings` | Deadline/edition calendar |

---

## OPEN

- School's own written media policy (should override this file where it exists)
- Print vs web-only distribution decision
- Faculty advisor sign-off process specifics
