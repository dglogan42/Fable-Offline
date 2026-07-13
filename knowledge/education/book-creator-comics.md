# Book Creator — comics feature (offline notes)

**Skill:** `book-creator-comics-kit`  
**Feature page:** [bookcreator.com/features/comics](https://bookcreator.com/features/comics/)  
**App:** [app.bookcreator.com](https://app.bookcreator.com) · teacher [sign-in/teacher](https://app.bookcreator.com/sign-in/teacher)  
**Org:** Book Creator / Tools for Schools, Inc. (schema on site)  

VERIFY LIVE. Not educational or legal advice. Not product endorsement.

---

## Page seed (comics feature)

**Title:** Make comics with Book Creator  
**Pitch:** Easy classroom comic books for students and teachers.

### Comic building blocks (marketing)

| Element | Notes |
|---------|--------|
| Panels | Layout comic books; layouts include double grid, 3-panel, 4-panel, diagonal sets |
| Images | Photo library or device camera into panels |
| Stickers | Library stickers; resize; blank stickers for custom text |
| Captions | Caption styles |
| Speech bubbles | Dialogue |
| Funky text / styles | Preset comic titles; customize; drop shadow, thought bubbles, borders |
| Onomatopoeia stickers | e.g. Bang!, OOH!, Crash!, Zoom!, Argh! (marketing examples) |
| Backgrounds | Solid + pattern demos (white, yellow, blue, dots, bang, lines) on feature page demos |

### Related links on site

- [For Teachers](https://bookcreator.com/teachers/)  
- [Schools & Districts](https://bookcreator.com/schools-districts/)  
- [Features](https://bookcreator.com/features/)  
- [Pricing](https://bookcreator.com/pricing/)  
- [Resources](https://bookcreator.com/resources/) · [Support](https://bookcreator.com/support/)  
- [How can we use comics in the classroom?](https://bookcreator.com/blog/2015/11/how-can-we-use-comics-in-the-classroom/)  
- Historical competition: [winners](https://bookcreator.com/blog/2016/05/comic-competition-winners-chosen/) · [finalists](https://bookcreator.com/blog/2016/04/comic-book-here-are-finalists/)  

---

## Classroom workflow seed

```text
Teacher library / free or school plan
  → Student accounts per school policy
  → Storyboard beats
  → Panels + photos/camera
  → Stickers + bubbles + captions
  → Style polish
  → Share/export → LMS (Classroom)
```

---

## Privacy / third-party (marketing HTML dump seed)

Public comics page may load (for auditors; VERIFY LIVE):

| Host / vendor | Role seed |
|---------------|-----------|
| googletagmanager.com | GTM (`GTM-NTTF6Z8` seen in dump) |
| consent.cookiebot.com | Cookie consent |
| js.hs-scripts.com / HubSpot | Marketing / CTA |
| widget.intercom.io | Support chat |
| fonts.googleapis.com / fonts.bunny.net | Fonts |

Use skill `privacy-host-map` for formal maps. Prefer school SSO; no student PII in git.

---

## Fable handoffs

| Goal | Skill |
|------|--------|
| Assign unit | `google-for-education` |
| Stop-motion alternative | `stop-motion-dev-kit` |
| Draw-frame hybrid | `animation-dev-kit` |

---

## Scaffold

```text
workspace/education/<class-slug>/
  notes.md          # unit goals only — no student books
```
