/**
 * Auckland CBD Wellness Retreat / Self-Care Program Brochure
 * Curated from Heart of the City Health & Wellbeing directory (heartofthecity.co.nz).
 * Not an official HOTC product; not medical advice. Book venues directly / VERIFY LIVE.
 */
const pptxgen = require("pptxgenjs");
const path = require("path");

const out = path.join(__dirname, 'Auckland_CBD_Wellness_Retreat_Brochure.pptx');

const C = {
  deep: "1A3A36",
  sage: "3D6B63",
  mist: "A8C5BE",
  cream: "F7F3EC",
  sand: "E8E0D4",
  clay: "C4785A",
  ink: "1F2A28",
  soft: "5A6B68",
  white: "FFFFFF",
  gold: "C4A574",
};

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Fable Offline (curated brochure)";
pres.title = "Auckland CBD Wellness Retreat — Self-Care Program Brochure";
pres.subject = "Curated from Heart of the City Health & Wellbeing";

function footer(slide, page, total) {
  slide.addText("Curated city-centre self-care  ·  heartofthecity.co.nz/health-wellbeing  ·  Not medical advice", {
    x: 0.5, y: 5.28, w: 7.5, h: 0.25,
    fontSize: 9, fontFace: "Calibri", color: C.soft, margin: 0,
  });
  slide.addText(`${page} / ${total}`, {
    x: 8.5, y: 5.28, w: 1.0, h: 0.25,
    fontSize: 9, fontFace: "Calibri", color: C.soft, align: "right", margin: 0,
  });
}

const TOTAL = 8;

// ─── 1 Cover ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.deep } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.clay } });
  s.addShape(pres.shapes.RECTANGLE, { x: 6.8, y: 0, w: 3.2, h: 5.625, fill: { color: C.sage } });
  s.addText("AUCKLAND CITY CENTRE", {
    x: 0.55, y: 1.15, w: 5.8, h: 0.35,
    fontSize: 12, fontFace: "Calibri", color: C.mist, charSpacing: 3, margin: 0,
  });
  s.addText("Wellness Retreat\n& Self-Care Program", {
    x: 0.55, y: 1.55, w: 5.9, h: 1.6,
    fontSize: 36, fontFace: "Georgia", color: C.cream, bold: true, margin: 0,
  });
  s.addText("A curated multi-day self-care itinerary using Heart of the City\nhealth & wellbeing offerings — spas, yoga, gyms, beauty & more.", {
    x: 0.55, y: 3.35, w: 5.8, h: 0.7,
    fontSize: 13, fontFace: "Calibri", color: C.mist, margin: 0,
  });
  s.addText("Brochure edition  ·  2026", {
    x: 0.55, y: 4.85, w: 5.5, h: 0.3,
    fontSize: 11, fontFace: "Calibri", color: C.gold, margin: 0,
  });
  s.addText("RESET\n·\nRESTORE\n·\nRETURN", {
    x: 7.1, y: 1.6, w: 2.6, h: 2.8,
    fontSize: 18, fontFace: "Georgia", color: C.cream, align: "center", bold: true, margin: 0,
  });
}

// ─── 2 Welcome ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.cream } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.12, fill: { color: C.sage } });
  s.addText("Welcome to your city-centre reset", {
    x: 0.5, y: 0.35, w: 9, h: 0.5,
    fontSize: 28, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
  });
  s.addText("Heart of the City’s Health & Wellbeing directory lists 100+ CBD options — gyms, yoga, pilates, spa & massage, hair and beauty — across Britomart, Queen Street, Wynyard Quarter, Victoria Park, Commercial Bay and more.", {
    x: 0.5, y: 1.0, w: 9, h: 0.75,
    fontSize: 14, fontFace: "Calibri", color: C.ink, margin: 0,
  });

  const cards = [
    { t: "Who it’s for", d: "Busy locals & visitors who want a structured self-care break without leaving the CBD." },
    { t: "Format", d: "Flexible 1–3 day “retreat in the city” — book experiences HITL with each venue." },
    { t: "Spirit", d: "Look and feel your best: restore body, calm mind, then re-enter the week with intention." },
  ];
  cards.forEach((c, i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y: 2.0, w: 2.95, h: 2.5,
      fill: { color: C.white },
      shadow: { type: "outer", color: "000000", blur: 6, opacity: 0.08, offset: 2 },
      rectRadius: 0.08,
    });
    s.addShape(pres.shapes.RECTANGLE, { x, y: 2.0, w: 2.95, h: 0.1, fill: { color: i === 1 ? C.clay : C.sage } });
    s.addText(c.t, {
      x: x + 0.18, y: 2.3, w: 2.6, h: 0.4,
      fontSize: 16, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
    });
    s.addText(c.d, {
      x: x + 0.18, y: 2.85, w: 2.6, h: 1.4,
      fontSize: 13, fontFace: "Calibri", color: C.soft, margin: 0,
    });
  });
  footer(s, 2, TOTAL);
}

// ─── 3 Six pillars ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.cream } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.12, fill: { color: C.sage } });
  s.addText("Six self-care pillars", {
    x: 0.5, y: 0.35, w: 9, h: 0.45,
    fontSize: 28, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
  });
  s.addText("Mapped to Heart of the City Health & Wellbeing categories", {
    x: 0.5, y: 0.85, w: 9, h: 0.3,
    fontSize: 13, fontFace: "Calibri", color: C.soft, italic: true, margin: 0,
  });

  const pillars = [
    { n: "01", t: "Move", d: "Gyms · group fitness · cycling · boxing · PT" },
    { n: "02", t: "Flow", d: "Yoga studios · hot yoga · mindful movement" },
    { n: "03", t: "Core", d: "Pilates studios for strength & alignment" },
    { n: "04", t: "Restore", d: "Spa · massage · body rituals · day spa" },
    { n: "05", t: "Glow", d: "Hair salons · beauty · skincare · nails" },
    { n: "06", t: "Nourish", d: "Supplements · healthy habits · city fuel" },
  ];
  pillars.forEach((p, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.5 + col * 3.15;
    const y = 1.35 + row * 1.7;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w: 3.0, h: 1.5,
      fill: { color: row === 0 ? C.deep : C.white },
      rectRadius: 0.08,
      shadow: row === 1 ? { type: "outer", color: "000000", blur: 5, opacity: 0.07, offset: 1 } : undefined,
    });
    s.addText(p.n, {
      x: x + 0.2, y: y + 0.2, w: 0.7, h: 0.35,
      fontSize: 14, fontFace: "Calibri", color: row === 0 ? C.gold : C.clay, bold: true, margin: 0,
    });
    s.addText(p.t, {
      x: x + 0.2, y: y + 0.55, w: 2.5, h: 0.35,
      fontSize: 18, fontFace: "Georgia", color: row === 0 ? C.cream : C.deep, bold: true, margin: 0,
    });
    s.addText(p.d, {
      x: x + 0.2, y: y + 0.95, w: 2.55, h: 0.4,
      fontSize: 12, fontFace: "Calibri", color: row === 0 ? C.mist : C.soft, margin: 0,
    });
  });
  footer(s, 3, TOTAL);
}

// ─── 4 3-day itinerary ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.cream } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.12, fill: { color: C.clay } });
  s.addText("Three-day self-care itinerary", {
    x: 0.5, y: 0.35, w: 9, h: 0.45,
    fontSize: 28, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
  });
  s.addText("Mix & match · book each venue directly · VERIFY LIVE hours & availability", {
    x: 0.5, y: 0.85, w: 9, h: 0.28,
    fontSize: 12, fontFace: "Calibri", color: C.soft, italic: true, margin: 0,
  });

  const days = [
    {
      day: "DAY 1",
      title: "Arrive & unwind",
      items: [
        "Morning: gentle walk waterfront / Wynyard",
        "Midday: spa or massage (Britomart / city)",
        "Afternoon: hair or skincare treat",
        "Evening: early rest · journal intentions",
      ],
    },
    {
      day: "DAY 2",
      title: "Move & strengthen",
      items: [
        "Morning: yoga or pilates class",
        "Midday: nourishing CBD lunch",
        "Afternoon: gym session or PT",
        "Evening: recovery stretch · light dinner",
      ],
    },
    {
      day: "DAY 3",
      title: "Integrate & glow",
      items: [
        "Morning: short flow or walk",
        "Midday: optional beauty / nails",
        "Afternoon: one favourite restore repeat",
        "Close: habit plan for the week ahead",
      ],
    },
  ];
  days.forEach((d, i) => {
    const x = 0.4 + i * 3.2;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y: 1.3, w: 3.05, h: 3.55,
      fill: { color: C.white },
      rectRadius: 0.08,
      shadow: { type: "outer", color: "000000", blur: 6, opacity: 0.08, offset: 2 },
    });
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: 1.3, w: 3.05, h: 0.85,
      fill: { color: i === 1 ? C.sage : C.deep },
    });
    s.addText(d.day, {
      x: x + 0.2, y: 1.4, w: 2.6, h: 0.3,
      fontSize: 11, fontFace: "Calibri", color: C.gold, charSpacing: 2, margin: 0,
    });
    s.addText(d.title, {
      x: x + 0.2, y: 1.7, w: 2.6, h: 0.35,
      fontSize: 16, fontFace: "Georgia", color: C.cream, bold: true, margin: 0,
    });
    s.addText(
      d.items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j < d.items.length - 1 } })),
      {
        x: x + 0.2, y: 2.4, w: 2.65, h: 2.2,
        fontSize: 12, fontFace: "Calibri", color: C.ink, valign: "top",
      }
    );
  });
  footer(s, 4, TOTAL);
}

// ─── 5 Featured venues ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.cream } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.12, fill: { color: C.sage } });
  s.addText("Sample venues from the directory", {
    x: 0.5, y: 0.3, w: 9, h: 0.4,
    fontSize: 26, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
  });
  s.addText("Illustrative picks listed on heartofthecity.co.nz/health-wellbeing — always confirm details live.", {
    x: 0.5, y: 0.75, w: 9, h: 0.3,
    fontSize: 12, fontFace: "Calibri", color: C.soft, italic: true, margin: 0,
  });

  const rows = [
    ["SO/ Spa", "Britomart", "Facials, body rituals & massages — urban underground calm"],
    ["Studio Red Yoga", "City", "Hot yoga with spa-like comfort (VERIFY LIVE listing)"],
    ["Chill Wellness", "City", "Cryotherapy, infrared sauna, red light & recovery tech"],
    ["JustWorkout 24HR", "Swanson St", "Gym, classes, yoga, pilates, boxing, PT"],
    ["Barclay Relax", "City", "Traditional & modern wellness techniques"],
    ["Feel Good Acupuncture", "City", "Acupuncture & wellness clinic services"],
    ["Servilles City Works", "Victoria Park", "Luxury hair experience"],
    ["Caci Wynyard Quarter", "Wynyard", "Personalised beauty treatments"],
  ];

  // table header
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.15, w: 9.0, h: 0.38, fill: { color: C.deep } });
  s.addText("Venue", { x: 0.6, y: 1.2, w: 2.4, h: 0.28, fontSize: 11, fontFace: "Calibri", color: C.cream, bold: true, margin: 0 });
  s.addText("Area", { x: 3.0, y: 1.2, w: 1.5, h: 0.28, fontSize: 11, fontFace: "Calibri", color: C.cream, bold: true, margin: 0 });
  s.addText("Why it fits the program", { x: 4.6, y: 1.2, w: 4.7, h: 0.28, fontSize: 11, fontFace: "Calibri", color: C.cream, bold: true, margin: 0 });

  rows.forEach((r, i) => {
    const y = 1.55 + i * 0.4;
    const bg = i % 2 === 0 ? C.white : C.sand;
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y, w: 9.0, h: 0.4, fill: { color: bg } });
    s.addText(r[0], { x: 0.6, y: y + 0.05, w: 2.4, h: 0.3, fontSize: 11, fontFace: "Calibri", color: C.deep, bold: true, margin: 0 });
    s.addText(r[1], { x: 3.0, y: y + 0.05, w: 1.5, h: 0.3, fontSize: 11, fontFace: "Calibri", color: C.sage, margin: 0 });
    s.addText(r[2], { x: 4.6, y: y + 0.05, w: 4.7, h: 0.3, fontSize: 11, fontFace: "Calibri", color: C.ink, margin: 0 });
  });
  footer(s, 5, TOTAL);
}

// ─── 6 Half-day express ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.cream } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.12, fill: { color: C.sage } });
  s.addText("Express options", {
    x: 0.5, y: 0.35, w: 9, h: 0.45,
    fontSize: 28, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
  });

  const opts = [
    { t: "Half-day Restore", d: "90-min massage or spa ritual + café pause + short waterfront walk. Ideal mid-week." },
    { t: "Morning Flow Pack", d: "Yoga or pilates class + protein / light breakfast nearby + optional infrared or stretch." },
    { t: "Glow Afternoon", d: "Hair or beauty appointment + nails or skincare + quiet hour with a book." },
    { t: "Active Reset", d: "Gym or PT block + recovery modality (sauna / compression if available) + hydrate." },
  ];
  opts.forEach((o, i) => {
    const y = 1.0 + i * 0.95;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: 0.5, y, w: 9.0, h: 0.85,
      fill: { color: C.white },
      rectRadius: 0.06,
    });
    s.addShape(pres.shapes.OVAL, {
      x: 0.7, y: y + 0.22, w: 0.42, h: 0.42,
      fill: { color: i % 2 === 0 ? C.sage : C.clay },
    });
    s.addText(String(i + 1), {
      x: 0.7, y: y + 0.28, w: 0.42, h: 0.3,
      fontSize: 14, fontFace: "Calibri", color: C.cream, align: "center", bold: true, margin: 0,
    });
    s.addText(o.t, {
      x: 1.35, y: y + 0.12, w: 7.8, h: 0.3,
      fontSize: 15, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
    });
    s.addText(o.d, {
      x: 1.35, y: y + 0.42, w: 7.8, h: 0.35,
      fontSize: 13, fontFace: "Calibri", color: C.soft, margin: 0,
    });
  });
  footer(s, 6, TOTAL);
}

// ─── 7 How to book + habits ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.cream } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 4.3, h: 5.625, fill: { color: C.deep } });

  s.addText("How to use this brochure", {
    x: 0.4, y: 0.45, w: 3.6, h: 0.9,
    fontSize: 22, fontFace: "Georgia", color: C.cream, bold: true, margin: 0,
  });
  const steps = [
    "Open heartofthecity.co.nz/health-wellbeing",
    "Filter by Gyms, Yoga, Spa, Hair…",
    "Pick precinct (Britomart, Queen St…)",
    "Book each venue yourself (HITL)",
    "Save favourites on the HOTC site",
    "Follow healthy-habits inspiration articles",
  ];
  steps.forEach((t, i) => {
    s.addText(`${i + 1}.  ${t}`, {
      x: 0.4, y: 1.5 + i * 0.5, w: 3.6, h: 0.45,
      fontSize: 13, fontFace: "Calibri", color: C.mist, margin: 0,
    });
  });

  s.addText("Self-care habit prompts", {
    x: 4.7, y: 0.45, w: 4.8, h: 0.45,
    fontSize: 22, fontFace: "Georgia", color: C.deep, bold: true, margin: 0,
  });
  s.addText("Inspired by city-centre wellbeing themes — personal, non-clinical:", {
    x: 4.7, y: 1.0, w: 4.8, h: 0.4,
    fontSize: 12, fontFace: "Calibri", color: C.soft, italic: true, margin: 0,
  });
  const habits = [
    { h: "Protect one appointment", b: "Treat spa/yoga like a meeting you cannot move." },
    { h: "Phone-down blocks", b: "30 minutes without notifications after a session." },
    { h: "Hydrate & walk", b: "Pair every treatment with water + 10-minute walk." },
    { h: "Sleep as recovery", b: "Earlier bedtime the night of intense training." },
    { h: "One weekly pillar", b: "Rotate Move / Flow / Restore so nothing drops off." },
  ];
  habits.forEach((h, i) => {
    const y = 1.5 + i * 0.65;
    s.addText(h.h, {
      x: 4.7, y, w: 4.8, h: 0.28,
      fontSize: 14, fontFace: "Georgia", color: C.sage, bold: true, margin: 0,
    });
    s.addText(h.b, {
      x: 4.7, y: y + 0.28, w: 4.8, h: 0.28,
      fontSize: 12, fontFace: "Calibri", color: C.ink, margin: 0,
    });
  });
  footer(s, 7, TOTAL);
}

// ─── 8 Closing ───
{
  const s = pres.addSlide();
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.deep } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.clay } });
  s.addText("Start where you are.\nRestore in the heart of the city.", {
    x: 0.7, y: 1.2, w: 8.5, h: 1.3,
    fontSize: 30, fontFace: "Georgia", color: C.cream, bold: true, margin: 0,
  });
  s.addText("Explore  ·  heartofthecity.co.nz/health-wellbeing", {
    x: 0.7, y: 2.7, w: 8, h: 0.4,
    fontSize: 16, fontFace: "Calibri", color: C.gold, margin: 0,
  });
  s.addText([
    { text: "Disclaimer: ", options: { bold: true } },
    { text: "This brochure is an independent curation for planning inspiration. It is not medical, physiotherapy, or mental-health advice, and is not an official Heart of the City package. Business listings, hours, and services change — VERIFY LIVE and book directly. For emergencies in New Zealand call 111. For health advice: Healthline / Health NZ pathways." },
  ], {
    x: 0.7, y: 3.4, w: 8.5, h: 1.2,
    fontSize: 11, fontFace: "Calibri", color: C.mist, margin: 0,
  });
  s.addText("Source: Heart of the City — Health and Wellbeing  ·  © HOTC listings remain with their owners", {
    x: 0.7, y: 4.9, w: 8.5, h: 0.3,
    fontSize: 10, fontFace: "Calibri", color: C.soft, margin: 0,
  });
}

pres.writeFile({ fileName: out }).then(() => {
  console.log("Wrote", out);
}).catch((e) => {
  console.error(e);
  process.exit(1);
});
