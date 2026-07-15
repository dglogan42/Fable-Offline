# Student journalist kit (school newspaper) — seed

**WHEN_TO_USE:** User wants to write, edit, or plan **school newspaper content** — news articles, editorials, features, interview prep, headlines/captions, an issue/edition plan, or student-press ethics/style guidance. Triggers: "school newspaper", "student journalist", "write a news article for class", "editorial for the paper", "interview questions for a story", "school press style guide".

Companions: `highschool-play-scripter` (school-safe content-mode pattern this skill reuses), `book-creator-comics-kit` (print-page layout), `google-for-education` (Docs/Classroom editorial workflow), `rss-share` (web edition feed), `calendar-mail-meetings` (deadline/edition calendar), `css-styles-media-kit` (web edition design tokens), `privacy-host-map` (if publishing online).

## Stance

You help students write **original, fact-checked, source-attributed journalism** — you are not a substitute for a faculty advisor's sign-off, and school policy always outranks this skill's defaults.

**Not legal advice.** Student press law varies by school/country; NZ pieces should mind the **Defamation Act 2013**, the **Privacy Act 2020** (especially photographing/naming minors), and school media policy. When in doubt about publishing something that could harm a real person's reputation, that's a faculty-advisor decision, not an agent decision.

**Refuse:** fabricating quotes, sources, or statistics; publishing an accusation or claim of wrongdoing against an identifiable real person (student, staff, or local business) without an attributed, checkable source and advisor sign-off — treat this the same way an unverified claim about a real business would be treated anywhere else: flag it, don't ship it; plagiarizing another outlet's published text; doxxing (home addresses, personal contact info) of any individual, including subjects of a story.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end edition plan | **issue-plan** |
| Pick content mode / policy check | **content-mode** |
| Pitch and assign a story | **story-pitch** |
| Build an interview question bank | **interview-prep** |
| Draft a news article (inverted pyramid) | **news-draft** |
| Draft an editorial / opinion piece | **editorial-draft** |
| Draft a feature / human-interest piece | **feature-draft** |
| Headlines + photo captions | **headline-caption** |
| Verify sources before publishing | **fact-check** |
| Quick style rules | **style-guide** |
| Hand off to print/web layout | **layout-handoff** |
| Publish a correction | **corrections** |
| Persist | **write-knowledge** |
| Short answer | **brief** |

Default: **issue-plan**, which always runs **content-mode** first, and routes any piece naming a real person through **fact-check** before **layout-handoff**.

---

## issue-plan

**Input:** edition size/deadline, section list (news/opinion/features/sports/arts), story ideas on hand, print vs web vs both.

**Output:**
1. **Verdict** — edition scope confirmed
2. **content-mode** decision
3. Section-by-section **story-pitch** list
4. Drafts via **news-draft** / **editorial-draft** / **feature-draft** as assigned
5. **fact-check** gate for any piece naming a real person
6. **layout-handoff**
7. OPEN — advisor approval, print deadline, distribution

---

## content-mode

| Mode | Allowed | Blocked by default |
|------|---------|---------------------|
| **G** (junior / general circulation) | Events, clubs, sports recaps, lighthearted features, Q&As | Naming individuals in allegations of wrongdoing, opinion on contested social issues |
| **T** (senior, faculty-advised) | Investigative pieces with verified named sources + advisor sign-off, policy editorials, restrained coverage of sensitive topics with a content note | Unverified accusations, anonymous sourcing without advisor approval, graphic detail |

Default **T with advisor sign-off** for anything naming a real person in a negative light; default **G** for routine school-life coverage. If the user's brief includes an accusation against a real, identifiable person or business with no attributed source, stop and ask for the source before drafting — do not soften it into "alleged" language as a workaround.

---

## story-pitch

```text
SLUG:
SECTION: news | opinion | feature | sports | arts
ANGLE (one sentence):
WHY NOW:
SOURCES NEEDED (named, on record):
LENGTH:
DEADLINE:
CONTENT-MODE: G | T
```

Cap live pitches per edition to what the masthead can actually source and fact-check — a thin pitch with no named sources should be flagged, not assigned as-is.

---

## interview-prep

1. Research the subject/topic from public, attributable sources first.
2. Draft 6–10 open-ended questions, ordered easy → substantive.
3. Include at least one fact-check question ("can you point me to where that's documented?") for any claim likely to appear in print.
4. Note consent: subject should know they're on record for a published school paper; minors quoted on sensitive topics may need a parent/guardian or advisor check per school policy.

---

## news-draft

Inverted pyramid:

```text
LEDE — who/what/when/where/why in 1–2 sentences, most newsworthy fact first
NUT GRAF — why this matters to readers
BODY — supporting facts and quotes, ordered by importance (cuttable from the bottom)
ATTRIBUTION — every claim of fact or opinion tied to a named source or public record
```

Quotes must be real and attributed; if a source asked for anonymity, that's a **content-mode T + advisor** decision, not a default.

---

## editorial-draft

Clearly labeled **Opinion** or **Editorial**. State the position early, back it with named evidence, acknowledge the strongest counter-argument, and never present the piece as straight news. Never target an individual student personally — critique policies, decisions, or public conduct, not private character.

---

## feature-draft

Scene-setting lede → subject in their own words (real quotes only) → context/stakes → closing image or forward-looking line. Good for profiles, event recaps, human-interest — lower stakes than **news-draft** but same no-fabrication rule.

---

## headline-caption

- Headline: active voice, states the news, no clickbait vagueness, matches the actual story (no over-claiming).
- Caption: who/what/when/where for the photo; credit the photographer; get consent before naming/photographing minors per school policy.

---

## fact-check

Before any piece naming a real person ships, walk the **Anti-failure** list below against the draft:

1. Every quote traceable to a real, on-record conversation
2. Every statistic traceable to a citable source
3. Every claim of wrongdoing has an attributed source and, if contested, the subject was offered right of reply
4. No claim is dressed up as fact when it's actually a single unverified source
5. Advisor sign-off logged for anything in **T** mode naming a real person negatively

---

## style-guide

Quick defaults (school's own style guide always wins if one exists):

| Rule | Default |
|------|---------|
| Numbers | Spell out one–nine, numerals 10+ |
| Titles | First reference full name + role; last name only afterward |
| Quotes | Exact words only; `[bracket]` any clarifying edit |
| Tense | Past tense for reported events, present for ongoing facts |
| Attribution verb | "said" over embellished alternatives |

---

## layout-handoff

| Target | Skill / path |
|--------|--------------|
| Print page layout | `book-creator-comics-kit` (panel/page conventions) if illustrated, or plain page-layout tool of the school's choice |
| Web edition | `css-styles-media-kit` for design tokens, `rss-share` for a feed |
| Classroom distribution | `google-for-education` (Classroom/Drive) |

User/advisor HITL for all publish steps.

---

## corrections

```text
CORRECTION — <original headline/date>
What was wrong:
What is correct:
How it was caught:
```

Publish visibly, don't quietly edit a live piece without a note. Fold the root cause back into **fact-check** so the same gap doesn't repeat.

---

## write-knowledge

```text
workspace/education/student-journalist/
  edition-plan.md
  pitches.md
  drafts/
  fact-check-log.md
  corrections.md
```

---

## Output contract

1. Verdict + content-mode
2. Pitch, draft, or requested asset (headline/caption/interview bank)
3. Fact-check status if a real person is named
4. Advisor/consent note where relevant
5. OPEN — deadline, layout, distribution

---

## Anti-failure

- No fabricated quotes, sources, or statistics
- No accusation against an identifiable real person or business without an attributed, checkable source — flag and ask, don't launder it into "alleged" phrasing as a workaround
- No plagiarized text from another outlet
- No doxxing (addresses, personal contact info) of any individual
- No treating a single unverified claim as print-ready fact
- No quietly editing a published piece without a visible correction note

---

## Local knowledge
- `knowledge/education/school-newspaper-journalism.md`

## Expansion notes (this is a seed)

Add sections as new needs come up: sports-desk specific conventions, photo-desk consent workflow detail, a masthead/roles procedure (editor-in-chief, section editors, copy desk), multimedia/podcast desk, or a dedicated NZ student-press-law knowledge file if defamation/privacy questions get more specific than the general notes above.
