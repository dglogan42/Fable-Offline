# University of Auckland — Eloqua postgraduate webinar landing page

**Compiled:** 2026-07-12  
**Page type:** Oracle Eloqua hosted landing page + lead form (not the main `www.auckland.ac.nz` CMS shell alone)  
**Title (document):** University of Auckland  
**Campaign (from tracking params):** `2026_eng_PG_Webinars_May26-August26` · content `Master-of-Urban-Design`  
**Form name:** `ENGDES-FS-PG-20260218-ONE-PG-Live-Webinars`  
**Skill:** `privacy-host-map`  
**Not legal advice.** Re-check live Network tab and UoA privacy notices before relying on this map.

---

## Verdict first

**Map only / partially verified (static HTML)** — clear **LOAD** and **CONFIG** for Oracle Eloqua marketing automation, first-party-looking UoA response/track hosts, Google Ads click attribution in the visitor pixel, and a lead form collecting contact + student status + webinar choices. No full browser Network capture; consent banner behaviour not visible in this dump.

**Purpose of page (content):** postgraduate webinar registration (Engineering / Design suite: Disaster Management, Urban Design, Energy, Medical Engineering, Design, Urban Planning (Professional), Engineering — July–August dates in body copy).

---

## Method

1. Static HTML dump of Eloqua landing page (form CSS, layout, footer, tracking pixel).  
2. Host classification per skill `privacy-host-map` legend.  
3. Form field inventory from visible labels + hidden Eloqua fields.

### Legend

| Tag | Meaning |
|-----|---------|
| **LOAD** | Script/iframe/img load on page |
| **CONFIG** | Form action / API / site IDs |
| **CLICK** | Outbound link (user-initiated) |
| **BUNDLE** | String in vendor assets only — not confirmed call |

### First-party / same-org family (UoA)

- `www.auckland.ac.nz` — main university site links  
- `response.auckland.ac.nz` — Eloqua-facing response / form post domain  
- `app.response.auckland.ac.nz` — tracked redirect links (footer policy links)  
- `images.response.auckland.ac.nz` — campaign images  
- `track.auckland.ac.nz` — named as **firstPartyCookieDomain** on Eloqua visitor pixel  

These are university-controlled or university-branded marketing infrastructure; **backend still runs on Oracle Eloqua** (`*.eloqua.com` / `en25.com`).

---

## A. High privacy relevance

| Host | Role | Tag | Notes |
|------|------|-----|--------|
| **s810866859.t.eloqua.com** | Eloqua visitor tracking pixel (`/visitor/v200/svrGP`) | **LOAD** | 1×1 image; `siteid=810866859`; `LandingPageID=1674`; `firstPartyCookieDomain=track.auckland.ac.nz`; carries **UTM + gclid** query string |
| **response.auckland.ac.nz** | Form POST + Eloqua landing | **CONFIG** / **LOAD** | Form `action=https://response.auckland.ac.nz/e/f2?LP=1674` |
| **app.response.auckland.ac.nz** | Tracked link redirects (`/e/er?…`) | **CLICK** | Footer Accessibility/Copyright/Privacy/Disclaimer go through Eloqua click-tracking params (`elqTrackId`, `elqaid=1674`, etc.) |
| **images.response.auckland.ac.nz** | Campaign banner images | **LOAD** | EloquaImages path under TheUniversityofAuckland client |
| **img07.en25.com** | Oracle Eloqua / Responsys CDN family | **LOAD** (if referenced) | Common Eloqua asset host |
| **track.auckland.ac.nz** | First-party cookie domain (named in pixel) | **CONFIG** | Cookie scope for marketing identity on university DNS |
| **www.googletagmanager.com** | GTM (string/host seen in dump) | **BUNDLE** / verify **LOAD** | Confirm in Network whether GTM actually loads on this LP |
| **code.jquery.com** | jQuery CDN (if used by form validation) | verify **LOAD** | Confirm live request |
| **Google Ads params** | `gclid`, `gad_source`, `gad_campaignid`, `gclsrc=aw.ds` | **CONFIG** (on pixel URL) | Paid search click ID pasted into Eloqua visitor beacon |

### Eloqua site identifiers (CONFIG)

| Field | Value (from dump) |
|-------|-------------------|
| `elqSiteId` | `810866859` |
| `elqFormName` | `ENGDES-FS-PG-20260218-ONE-PG-Live-Webinars` |
| Landing page | `LP=1674` / `LandingPageID=1674` |
| Form id | `form1414` |
| Campaign hidden | `elqCampaignId` (empty in dump; server may fill) |

---

## B. Personal data the form requests (lead capture)

| Field (visible) | Sensitivity |
|-----------------|-------------|
| First name | Identity |
| Last name | Identity |
| Email * | Contact (required) |
| Mobile phone | Contact |
| “Which statement describes you best?” | Student status / domestic vs international / working professional |
| Webinar multi-select | Programme interest (e.g. Master of Urban Design) |
| `address1` | Present in form markup (honeypot or address — treat as PII if user-visible) |

**Hidden marketing fields:** Eloqua form name, site ID, submission token, campaign ID.

Submitting the form is an intentional **marketing lead** submission to UoA/Eloqua — higher sensitivity than passive analytics.

---

## C. Campaign attribution (on tracking pixel URL)

Observed query parameters on the Eloqua visitor image:

| Param | Example meaning |
|-------|-----------------|
| `utm_source` | `google` |
| `utm_medium` | `search` |
| `utm_campaign` | `2026_eng_PG_Webinars_May26-August26` |
| `utm_content` | `Master-of-Urban-Design` |
| `gclid` | Google Ads click identifier (long) |
| `gad_campaignid` | `23881680913` |
| `optin` | `disabled` on pixel (Eloqua opt-in flag for that beacon — **not** a claim about email consent law) |

---

## D. Social / other

| Host | Tag | Notes |
|------|-----|--------|
| **github.com** | **BUNDLE** | Likely normalize.css / license reference only |
| Footer policy labels | **CLICK** | Accessibility, Copyright, Privacy, Disclaimer — via **tracked** `app.response.auckland.ac.nz` URLs |

---

## E. Bundle noise

- `github.com` (normalize.css credit path)  
- Any other vendor doc hosts inside Eloqua CSS/JS not confirmed as runtime calls  

---

## Purpose diagram

```text
[User] ←Google Ads click (gclid/utm)→ [Eloqua landing LP=1674]
              │
              ├─LOAD→ s810866859.t.eloqua.com  (visitor pixel + gclid/utm)
              ├─CONFIG cookie domain→ track.auckland.ac.nz
              ├─LOAD→ images.response.auckland.ac.nz
              ├─POST form→ response.auckland.ac.nz/e/f2?LP=1674
              │              (name, email, phone, status, webinars)
              └─CLICK footer→ app.response.auckland.ac.nz/e/er?… (tracked)

Optional verify:
              ├─?→ www.googletagmanager.com
              └─?→ code.jquery.com
```

---

## Sensitive / hygiene notes

| Topic | Assessment |
|-------|------------|
| **Marketing automation** | Full Eloqua stack: site ID, form post, visitor pixel, tracked links |
| **First-party cookie domain** | Explicitly `track.auckland.ac.nz` — marketing ID may persist on university DNS |
| **Paid media join** | `gclid` on Eloqua pixel joins **Google Ads click** to **Eloqua visitor** profile when pixel fires |
| **Lead form** | Contact + student segment + programme interest — classic CRM feed |
| **Footer Privacy link** | Goes through Eloqua click-tracking wrapper (extra tracking hop before policy page) |
| **`optin=disabled` on pixel** | Technical Eloqua parameter; **do not** read as “opt-in not required” for PECR/Privacy Act email rules |

---

## What to verify next (primary)

1. DevTools **Network**: confirm GTM/jQuery actually load; list Set-Cookie for `track.auckland.ac.nz` and Eloqua hosts.  
2. Published privacy notices: UoA privacy + any marketing/enrolment collection statement on or linked from the LP.  
3. Whether webinar registration email uses double opt-in / unsubscribe (not in HTML).  
4. Data retention and CRM systems behind Eloqua (Sales/Service Cloud, student CRM, etc.).  
5. Google Ads ↔ Eloqua enhanced conversions / offline conversion config (beyond this HTML).  

---

## One concrete risk of trusting a short privacy footer alone

Assuming “Privacy” in the footer means **no marketing profiling** is false on this page: the HTML actively implements **Eloqua visitor tracking**, **Google Ads click ID capture**, and a **lead form** posting PII to `response.auckland.ac.nz` under site `810866859`. The privacy link itself is often opened via a **tracked** redirect.

---

## Related

- Skill: `skills/privacy-host-map.md`  
- Compare: `knowledge/privacy/akl-libraries-third-party-hosts.md` (council library tags vs university Eloqua lead-gen)

**Not legal advice. Snapshot may drift when LandingPageID, form name, or pixel params change.**
