# Privacy host map seed — Sport Auckland Green Prescription (GRx)

**Skill:** `privacy-host-map` · `green-prescription-grx-kit`  
**URL:** https://www.sportauckland.org.nz/sportauckland/green-prescription/green-prescription-grx  
**Evidence:** HTML dump (Sporty CMS, GA, GPT, Facebook SDK, Google Maps, Raygun).  

Not legal advice. VERIFY LIVE. Health referral data is sensitive — do not store clinical histories in git.

---

## Host inventory

| Host | Class | Notes |
|------|-------|--------|
| `www.sportauckland.org.nz` | LOAD/CLICK | GRx pages, forms, contact |
| `prodcdn.sporty.co.nz` | LOAD | CMS assets, logo, favicon |
| `www.sporty.co.nz` | CLICK | Platform branding / admin login |
| `www.google-analytics.com` | LOAD | UA-8182010-11 |
| `www.googletagmanager.com` | LOAD | gtag G-KH331M994Q |
| `www.googletagservices.com` | LOAD | GPT ads (`/44071230/SportyBanner`) |
| `connect.facebook.net` | LOAD | FB SDK v21; app id 849632328416506 |
| `maps.googleapis.com` | LOAD | Maps JS API |
| `use.typekit.net` | LOAD | Adobe fonts |
| `cdn.iframe.ly` | LOAD | Embed helper |
| `www.youtube.com` | LOAD/CLICK | Embedded GRx videos |
| `www.facebook.com` | CLICK | GreenPrescriptionAKLD |
| `harboursport.co.nz` | CLICK | West/North GRx alternative |
| Outlook safelinks | CLICK | Wrapped harbour sport URL |

### First-party path families

- `/sportauckland/green-prescription/*` · `/Green-Prescription/*`  
- `/contact/*`  
- `/bundles/sporty-styles` · `/bundles/sporty-scripts`  

---

## Notes

- Self-refer / professional referral forms may collect **health information** — user HITL only  
- GPT ads targeted Region=Auckland, OrgType=Rso  
- Do not republish live Maps API keys as “secrets to use”; rotate if abused  

## OPEN

- Cookie consent UX  
- Form processor hosts after submit  
- Full data retention policy for GRx referrals  
