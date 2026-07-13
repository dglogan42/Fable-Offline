# MIT License

Copyright (c) 2026 David Logan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Additional notices

These notices do **not** limit the MIT grant above.

### 1. Domain knowledge and skills

Markdown under `knowledge/` and `skills/` is provided for research, education,
and offline agent operations. It is **not professional advice**. In particular
it is not financial, investment, legal, medical, planning, customs,
biosecurity, veterinary, real-estate, or emergency-response advice, and it
does not create a professional-client relationship.

### 2. Third-party content

Snapshots that summarise public websites, policies, or PDFs (including
government and institutional materials) remain the property of their
respective rights holders. Fable Offline does not claim ownership of those
third-party works. Always re-verify against primary official sources.

### 3. Emergency and safety

In an emergency in New Zealand, call **111**. Agents must not take crime,
fire, or medical reports as the agent of record.

### 4. Steam, games, and local soak tests

Scripts such as `scripts/steam_launch.py` and `scripts/steam_sim_soak.py`,
and notes under `knowledge/steam/`, are helpers for launching games the user
**already owns and has installed**, and for measuring local model performance
under concurrent load.

They are **not** a game bot, multiplayer cheat, DRM bypass, or tool for
unauthorised access. Steam, individual games, trademarks, and related
software remain the property of Valve Corporation and the respective
publishers/developers. Launch only software you are licensed to run.

### 5. Calendar, mail, meetings, and Zoom

Notes under `knowledge/calendar/`, skill `calendar-mail-meetings`, and
`scripts/ical_parse.py` help with **local** iCalendar (`.ics`) files, meeting
prep, draft mail, and join **checklists**.

| Vendor surface | Example | Fable role |
|----------------|---------|------------|
| Google Calendar | [calendar.google.com](https://calendar.google.com/) | Prep / drafts; no authenticated scrape |
| Google Meet | `meet.google.com` | Flag as user CLICK from invites |
| Zoom Web Client | [app.zoom.us/wc/join](https://app.zoom.us/wc/join) | **join-zoom** checklist; never auto-join |

Google Calendar, Gmail, Meet, and related services remain the property of
Google LLC. Zoom Web Client and related services remain the property of Zoom
Video Communications, Inc. The Software does not grant rights to those
services and is not a substitute for their terms of service.

Do **not** commit OAuth tokens, app passwords, Zoom passcodes or `pwd=` query
values, secret iCal feed URLs, or full mailbox exports. Prefer
`knowledge/calendar/_local/` (gitignored) for private material.

### 6. Contributions

By submitting contributions to this repository, you agree they are licensed
under the same MIT License terms as the Software, unless you state otherwise
in writing with the copyright holders.

---

The plain-text file [`LICENSE`](LICENSE) contains the same MIT grant and
notices for tooling that expects a non-markdown license file.
