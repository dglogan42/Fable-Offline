# TikTok Creative Exchange (TTCX)

**Skill:** `tiktok-ads-create` (procedure **ttcx-brief**) · companion to campaign creation  
**Product:** Marketplace connecting **advertisers** with **creative service partners** for native TikTok-style ad videos  
**Portal (HTML dump):** title *TikTok Creative Exchange* · meta: “marketplace for connecting advertisers with creative service providers”  
**Official help:** [About TTCX for advertisers](https://ads.tiktok.com/help/article/tiktok-creative-exchange) (last updated March 2026 in fetch)  
**Portal path family:** [ads.tiktok.com/creativeexchange](https://ads.tiktok.com/creativeexchange) · PC path often `/creativeexchange/pc`  
**Not legal or contract advice.** VERIFY LIVE availability, pricing, and terms.

---

## Verdict

TTCX is TikTok’s **structured creative production marketplace**, not Ads Manager itself. Advertisers submit briefs, match partners, collaborate, receive assets, then run those creatives via **Campaign → Ad group → Ad** (`knowledge/ads/tiktok-ads-create.md`).

| Fact (help + dump) | Detail |
|--------------------|--------|
| Audience | Advertisers (help: **managed accounts** globally — contact account manager) |
| Value | Produce **volume** of native-feeling TikTok video creative with vetted partners |
| Process | Brief → source/select partner → collaborate → asset submission → feedback → tracking |
| Related ads stack | Pixel/Events still for measurement; TTCX is **creative supply** |

---

## How it works (advertiser)

From official help benefits:

1. Submit a **project brief**  
2. **Source and select** a creative partner (recommendations by need / vertical / market)  
3. **Manage collaboration**  
4. **Asset submission**  
5. **Feedback**  
6. **Progress tracking**  

Marketing page framing: match partners to creative needs; content that **feels native** to TikTok.

---

## Package types (help table)

| Family | Package | Description (summarised) |
|--------|---------|---------------------------|
| **VCP** Video Content Packages | **Net New** | New video content with talent(s); partner manages concept → delivery |
| **VCP** | **Remix** | Edit existing brand/agency assets to TikTok standards (resize, captions, etc.) |
| **CLP** Creator Led Packages | **Fixed** | Set number of creator-hosted videos by budget/needs |
| **CLP** | **Customized** | Specific outputs or higher volume |

### Add-ons (help)
- **Add-on services** — customisable options  
- **Subscription** — always-on work with preferred partner  
- **Fully funded creatives** — TikTok may fund standard packages for advertisers meeting requirements; **case-by-case**; account manager  

---

## Non-TTCX / off-platform packages (terms theme)

Dump includes multi-language **Advertiser Terms** excerpts (e.g. Portuguese): **Pacotes Não-TTCX** — packages whose fees/terms are set by the creative partner; advertiser may pay media + partner compensation; may contract **outside** the platform; **TTCX programme benefits may not apply**. TikTok positions as **intermediary** for in-programme work; not liable for partner/talent actions or assets in the same way as pure marketplace intermediation language — **read live terms**, do not rely on dump excerpts alone.

Live term links (help Resources):

- [TTCX Terms of Service (advertiser platform)](https://ads.tiktok.com/creativeexchange/terms/advertiser-platform-agreement)  
- [Content Production Package Terms](https://ads.tiktok.com/creativeexchange/terms/video-content-package-agreement)  

TikTok may cancel campaigns/briefs or prohibit participation if content violates Advertiser Terms / Agreement or is unsuitable — **VERIFY LIVE**.

---

## Migration: TikTok One Partner Exchange

Help (March 2026): TTCX functionality is **migrating to TikTok One** under **Partner Exchange**. Advertisers encouraged to transition when banner/instructions appear. TTCX remains for a limited time after Partner Exchange launch.  
Learn more: [About TikTok One Partner Exchange for advertisers](https://ads.tiktok.com/help/article/about-tiktok-one-partner-exchange-for-advertisers).

**Fable implication:** prefer “creative marketplace / Partner Exchange / TTCX” language; re-check which portal is current before coaching URLs.

---

## Case studies (help links — external PDFs)

- Fabletics  
- Next College Student Athlete  
- Taco Bell  

Hosted on ByteDance CDN paths under `tcex` objects — marketing only; not reproduced here.

---

## Relationship to Ads creation

```text
TTCX / Partner Exchange     → produce native video assets
        ↓
TikTok Ads Manager          → Campaign → Ad group → Ad (spend)
        ↓
Pixel / Events              → measure (tiktok-analytics)
```

| Skill | Role |
|-------|------|
| `tiktok-ads-create` | Media buy structure + launch |
| **ttcx-brief** (procedure) | Marketplace brief + package choice |
| `tiktok-analytics` | Landing measurement |
| Fit / outfit skills | In-house UGC alternative to TTCX |

---

## Privacy / platform notes (from HTML dump)

Dump head includes:

| Signal | Notes |
|--------|--------|
| `google-site-verification` | Present |
| `#pumbaa-rule` JSON | Client privacy/consent **rule engine** (cookie blockers, sample rates, network intercepts for GA/FB/LinkedIn/**analytics.tiktok.com** pixel consent errors, battery_info stripping, etc.) |
| Domains in rules | `tiktok.com`, `tiktokv.com` |
| MCS list endpoints | Multiple regional `mcs-*.tiktok.com` / `tiktokv.com` logging endpoints in rawVal |

Full host map: `knowledge/privacy/ttcx-hosts.md`.

---

## Re-verify before advising

1. Managed-account eligibility in market  
2. Whether TTCX or Partner Exchange is primary  
3. Funded-creative eligibility  
4. Package SLAs / delivery days (often partner-specific)  
5. Live Advertiser Terms  

---

## Cross-links

- Ads playbook: `tiktok-ads-create.md`  
- Pixel: `../privacy/tiktok-analytics.md`  
- UI CSS: `../web/css-design-fingerprint-tiktok-ui.md`  
