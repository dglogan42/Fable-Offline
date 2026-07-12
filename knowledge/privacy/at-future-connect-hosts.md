# Auckland Transport Future Connect — third-party host map

**Compiled:** 2026-07-12  
**App:** Future Connect Mapping Portal  
**Title:** Future Connect  
**Operator (content):** Auckland Transport (AT) — `at.govt.nz/FutureConnect`  
**Skill:** `privacy-host-map`  
**Related:** urban transport strategy UI; GIS stack (Esri ArcGIS JS)  
**Not legal advice.** Re-check live Network tab; map services often load additional ArcGIS Online / enterprise endpoints not listed in static HTML.

---

## Verdict first

**Map only (static HTML)** — public **interactive mapping portal** for AT’s **Future Connect** long-term transport plan. Loads **Esri ArcGIS JS API 4.21**, **Google Analytics 4** (`G-QZXSBZ5249`), Font Awesome CDN, local minified app JS/CSS, and a splash gate requiring **Terms & Conditions + Privacy Policy** agreement before portal use. Feedback form collects **comment + name** (PII) when enabled. Full layer/feature service URLs live in `js/script.min.js` (not in this dump).

---

## Product purpose (from splash copy)

Future Connect = long-term plan for **Auckland’s transport system**. Three key outputs:

1. **Strategic Networks** — most important links per mode  
2. **Transport System Analysis** — deficiencies and opportunities  
3. **Focus Areas** — regional transport challenges  

UI modes: Integrated Network, Cycle/Micromobility, Public Transport, Freight, General Traffic, Walking; periods **Current** vs **First Decade**; optional contextual layers / supporting networks; intermodal problems (Environment, Safety, Equity) when Transport System Analysis selected.

Official overview: https://at.govt.nz/FutureConnect  

Privacy policy link on splash: https://at.govt.nz/about-us/about-this-site/customer-privacy-policy/

---

## Legend

| Tag | Meaning |
|-----|---------|
| **LOAD** | Script/CSS/img loaded by page |
| **CONFIG** | IDs / behaviours in HTML |
| **CLICK** | User-initiated outbound |
| **BUNDLE** | Likely only inside minified app JS (verify Network) |

### First-party / same deployment

Relative assets (same origin as the portal host — **exact host not in dump**; often AT/ArcGIS-hosted):

- `styles/calcite-web.min.css`, `styles/style.min.css`, `styles/introjs.min.css`  
- `js/intro.min.js`, `js/script.min.js`  
- `images/*` (logo, waiting gif, favicon)  

Treat portal origin as **first-party AT (or AT vendor host)** once known from live URL.

---

## A. High privacy relevance

| Host / asset | Role | Tag | Notes |
|--------------|------|-----|--------|
| **www.googletagmanager.com** | gtag.js GA4 | **LOAD** | `G-QZXSBZ5249` — Google Analytics 4 |
| **Google Analytics measurement** | Page/view events | **CONFIG** / runtime | `gtag('config', 'G-QZXSBZ5249')` — typically hits `google-analytics.com` / `analytics.google.com` (confirm Network) |
| **js.arcgis.com** | ArcGIS JS API **4.21** + light theme CSS | **LOAD** | Esri CDN — map runtime, widgets |
| **stackpath.bootstrapcdn.com** | Font Awesome 4.7 CSS | **LOAD** | CDN font/icons |
| **Portal origin** `js/script.min.js` | App logic, layer URLs, map config | **LOAD** | **Primary place** for feature service endpoints, basemaps, edit layers |
| **AT.govt.nz** | Future Connect site + privacy policy | **CLICK** | Overview + privacy |

### Consent / splash gate

| Control | Behaviour |
|---------|-----------|
| Terms + Privacy checkbox | Required before **I agree** enabled (`onAgreeCheck`) |
| Guided help checkbox | Default **checked** — intro.js tour on agree |
| Privacy Policy | External AT page (new tab) |
| Terms | In-app help topic `faq99_desc` |

**Note:** GA4 script is in `<head>` **before** splash agree — analytics may fire on load **regardless** of “I agree” unless blocked elsewhere (consent mode not visible in HTML). Treat as a **tension** for privacy review.

---

## B. Personal data surfaces

| Surface | Fields | Sensitivity |
|---------|--------|-------------|
| Feedback form `#formFeedback` | Comment (max 1000), Name (max 150) | PII + free text |
| Map notes / editor | Present in DOM but much UI **commented out** | May be disabled in this build |
| Guided tour / local state | intro.js; checkbox prefs | Low; may use storage in min JS |

Feedback submit: `formFeedbackSubmit` — destination URL **not in HTML** (likely in `script.min.js` or ArcGIS feature layer applyEdits).

---

## C. Functional stack (non-ads)

| Component | Role |
|-----------|------|
| **ArcGIS Maps SDK for JS 4.21** | 2D/3D map view `#viewDiv`, widgets, legend |
| **Calcite Web** | Esri design system CSS (local) |
| **intro.js** | Guided tour (`intro.min.js`) |
| **Jimu-style splash** | `jimu-widget-splash` class names — Web AppBuilder / Experience-style splash pattern |
| **Font Awesome** | Icons |

---

## D. Bundle / Network follow-ups (not in static HTML)

Expect additional hosts when map starts (verify live):

- `*.arcgis.com` / `services*.arcgis.com` — basemaps, feature/map services  
- Possible **Auckland Transport / council enterprise ArcGIS** endpoints  
- Geocoding / geometry / print services  
- Any feedback feature service URL  

Do **not** invent service URLs; extract from `script.min.js` or Network.

---

## Purpose diagram

```text
[User browser]
    ├─LOAD→ googletagmanager.com/gtag/js?id=G-QZXSBZ5249  (GA4)
    ├─LOAD→ js.arcgis.com/4.21/  (Esri Maps SDK)
    ├─LOAD→ stackpath.bootstrapcdn.com  (Font Awesome)
    ├─LOAD→ same-origin js/script.min.js  (layers, app)
    ├─CLICK→ at.govt.nz/FutureConnect
    ├─CLICK→ at.govt.nz/.../customer-privacy-policy/
    └─(after agree) map tiles/features → ArcGIS services (TBD Network)
         optional feedback → name + comment → TBD endpoint
```

---

## Sensitive tensions

| Issue | Detail |
|-------|--------|
| **Analytics before consent** | GA4 loads in head; splash agree is for portal T&Cs, not clearly a cookie consent gate for Google |
| **Name + comment feedback** | Direct PII collection; retention/destination unknown from HTML |
| **Map interaction telemetry** | Esri + custom JS may log extent/layer toggles — check Network + AT privacy policy |
| **Long-term transport data** | Strategic network layers are public planning info, not inherently PII; feedback is |

---

## Urban / planning note

This portal is a **spatial decision-support UI** for regional transport strategy (aligns with `urban-planner-competencies`: GIS, strategic networks, multimodal planning, equity/safety/environment themes). Competence coaching ≠ endorsing specific network designations.

---

## What to verify next

1. Live URL of the portal (for first-party host name).  
2. Network: all `arcgis.com` / custom service hosts after load.  
3. Whether GA4 waits for consent (Consent Mode / GTM) — HTML suggests **no**.  
4. Feedback POST target and retention.  
5. Contents of Terms (`faq99_desc`) and AT privacy policy sections on analytics.  
6. Optional: fetch `js/script.min.js` for service URL inventory (BUNDLE→LOAD confirmation).  

---

## One concrete risk

Assuming “I agree” only opens a map with **no tracking** is false: **GA4 is already configured on page load**, and the portal depends on **Esri cloud CDN** plus (almost certainly) remote map services. The agreement covers T&Cs/privacy **policy links**, not a technical block on third-party tags.

---

## Related Fable

- Skill: `privacy-host-map`, `privacy-design-planner`  
- Urban: `urban-planner-competencies`, `knowledge/urban-planning/competencies.md`  
- Compare: `akl-libraries-third-party-hosts.md` (AEM+Coveo), `uoa-eloqua-pg-webinar-hosts.md` (Eloqua leads)

**Not legal advice. Snapshot may drift when ArcGIS version or GA ID changes.**
