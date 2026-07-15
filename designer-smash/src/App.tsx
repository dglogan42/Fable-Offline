import { useEffect, useState } from "react";
import { Analytics } from '@vercel/analytics/react';

function useMidnightCountdown() {
  const [remaining, setRemaining] = useState(getRemaining());

  function getRemaining() {
    const now = new Date();
    const next = new Date(now);
    next.setHours(24, 0, 0, 0);
    return Math.max(0, next.getTime() - now.getTime());
  }

  useEffect(() => {
    const id = setInterval(() => setRemaining(getRemaining()), 1000);
    return () => clearInterval(id);
  }, []);

  const totalSeconds = Math.floor(remaining / 1000);
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${pad(h)}:${pad(m)}:${pad(s)}`;
}

const archive = [
  { day: "Mon", brief: "Boarding pass, one way to nowhere", state: "done" },
  { day: "Tue", brief: "A weather app for liars", state: "done" },
  { day: "Wed", brief: "Onboarding for a haunted house", state: "done" },
  { day: "Thu", brief: "Receipt for a stolen idea", state: "done" },
  { day: "Fri", brief: "Loading screen that never lies", state: "done" },
  { day: "Today", brief: "Boarding pass, one way to nowhere", state: "live" },
];

const showcase = [
  { initials: "IK", handle: "@ilse.k", brief: "Haunted onboarding", sparks: 214 },
  { initials: "MR", handle: "@marco.types", brief: "Liar's weather app", sparks: 189 },
  { initials: "RC", handle: "@reyna.codes", brief: "Stolen-idea receipt", sparks: 172 },
  { initials: "TP", handle: "@tempo.paz", brief: "Loading, no lies", sparks: 158 },
  { initials: "JV", handle: "@jvoss", brief: "Haunted onboarding", sparks: 141 },
  { initials: "AO", handle: "@aoyelaran", brief: "Liar's weather app", sparks: 126 },
];

export default function App() {
  const countdown = useMidnightCountdown();
  const [email, setEmail] = useState("");
  const [invited, setInvited] = useState(false);

  function handleInvite(e: React.FormEvent) {
    e.preventDefault();
    if (!email.trim()) return;
    setInvited(true);
  }

  return (
    <>
      <header className="nav">
        <div className="nav__wrap">
          <a className="wordmark" href="#top">
            DESIGNER <span>SMASH</span>
          </a>
          <nav className="nav__links" aria-label="Primary">
            <a href="#brief">Challenges</a>
            <a href="#community">Community</a>
            <a href="#archive">Archive</a>
          </nav>
          <div className="nav__auth">
            <a className="nav__login" href="#join">Log in</a>
            <a className="btn btn--small" href="#join">Join free</a>
          </div>
        </div>
      </header>

      <main id="top">
        <section className="hero">
          <div className="hero__copy">
            <p className="eyebrow eyebrow--live">
              <span className="dot" aria-hidden="true" />
              Brief #142 &middot; live now
            </p>
            <h1 className="hero__title">
              Pressure makes
              <br />
              better designers.
            </h1>
            <p className="hero__sub">
              Designer Smash is the elite community that shows up daily &mdash; one brief,
              one deadline, no do-overs. Solve it, post it, and watch your thinking
              level up in public.
            </p>
            <div className="hero__ctas">
              <a className="btn btn--accent" href="#brief">Enter today&rsquo;s brief</a>
              <a className="btn btn--ghost" href="#how">See how it works &rarr;</a>
            </div>
          </div>

          <div className="ticket" id="brief">
            <div className="ticket__top">
              <span className="ticket__label">Admit one</span>
              <span className="ticket__label">Brief #142</span>
            </div>
            <h2 className="ticket__title">
              Redesign a boarding pass for a one&#8209;way trip to nowhere.
            </h2>
            <dl className="ticket__meta">
              <div>
                <dt>Category</dt>
                <dd>UI / UX</dd>
              </div>
              <div>
                <dt>Difficulty</dt>
                <dd aria-label="3 out of 5">
                  <span className="pips" aria-hidden="true">
                    <i className="on" /><i className="on" /><i className="on" /><i /><i />
                  </span>
                </dd>
              </div>
              <div>
                <dt>Time limit</dt>
                <dd>45:00</dd>
              </div>
            </dl>
            <div className="ticket__stub">
              <span>Drops in</span>
              <span className="ticket__countdown">{countdown}</span>
            </div>
          </div>
        </section>

        <section className="how" id="how">
          <ol className="how__steps">
            <li>
              <span className="how__num">01</span>
              <h3>Drop</h3>
              <p>One brief posts at midnight, same time for everyone. No preview, no prep.</p>
            </li>
            <li>
              <span className="how__num">02</span>
              <h3>Sprint</h3>
              <p>A fixed clock &mdash; usually 45 minutes &mdash; forces real decisions instead of tenth revisions.</p>
            </li>
            <li>
              <span className="how__num">03</span>
              <h3>Post</h3>
              <p>Submit as-is. The community reacts, comments, and remembers who showed up.</p>
            </li>
          </ol>

          <div className="archive" id="archive" aria-label="This week's briefs">
            {archive.map((item) => (
              <div className={`archive__chip archive__chip--${item.state}`} key={item.day}>
                <span className="archive__day">{item.day}</span>
                <span className="archive__brief">{item.brief}</span>
              </div>
            ))}
          </div>
        </section>

        <section className="showcase" id="community">
          <div className="showcase__head">
            <h2>Today&rsquo;s submissions</h2>
            <p>A live look at who showed up for Brief #142.</p>
          </div>
          <div className="showcase__strip" role="list">
            {showcase.map((s, i) => (
              <article className="subcard" role="listitem" key={i}>
                <div className="subcard__avatar" aria-hidden="true">{s.initials}</div>
                <p className="subcard__handle">{s.handle}</p>
                <p className="subcard__brief">{s.brief}</p>
                <p className="subcard__sparks">
                  <span>{s.sparks}</span> sparks
                </p>
              </article>
            ))}
          </div>
        </section>

        <section className="cta" id="join">
          <h2>Enter the arena.</h2>
          <p>Invites open in waves &mdash; drop your email and we&rsquo;ll send the next one.</p>
          {invited ? (
            <p className="cta__confirm">You&rsquo;re on the list. We don&rsquo;t have a launch date yet &mdash; we&rsquo;ll email you when we do.</p>
          ) : (
            <form className="cta__form" onSubmit={handleInvite}>
              <label className="sr-only" htmlFor="email">Email address</label>
              <input
                id="email"
                type="email"
                required
                placeholder="you@studio.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <button className="btn btn--accent" type="submit">Get an invite</button>
            </form>
          )}
        </section>
      </main>

      <footer className="footer">
        <a className="wordmark wordmark--small" href="#top">
          DESIGNER <span>SMASH</span>
        </a>
        <nav aria-label="Footer">
          <a href="#brief">Challenges</a>
          <a href="#community">Community</a>
          <a href="#archive">Archive</a>
        </nav>
        <p>&copy; 2026 Designer Smash. Built and deployed via GitHub.</p>
      </footer>
      <Analytics />
    </>
  );
}
