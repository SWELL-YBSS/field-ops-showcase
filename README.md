# Field Ops — Portfolio Showcase

A standalone, sending-disabled copy of a real client build ("TJC Field
Ops" — a mobile PWA field-inspection tool), kept here purely to show off
the work. It's a snapshot, not a maintained fork: the live client project
lives in a separate private repo and this one won't track further changes
to it.

Everything about the app is real and fully interactive — the 5-step
inspection wizard, offline support, PDF generation, the install banner,
the animated success screen — except the final "send" step, which is
hard-disabled here (see "Demo mode" below) so nothing ever leaves the
browser or reaches a real inbox.

## Demo mode

`DEMO_MODE = true` is hardcoded near the top of the script in
`checklist_source.html`. When set, `buildSummaryAndSubmit()` skips PDF
generation and the network call entirely and just shows the success
screen after a short delay — so the button, the animation, and the
copy all work exactly like the real thing, but nothing is sent
anywhere. A yellow ribbon at the top of every page makes this obvious
to anyone clicking through.

The real client build doesn't have this flag at all — it's specific to
this showcase copy, added deliberately so this repo can be shared,
deployed, and clicked through freely without any risk of contacting the
client or leaking their details.

## Files

- `index_source.html` — editable source for the home/job-select page.
  Edit this, not `index.html`.
- `checklist_source.html` — editable source for the Mine Ute Inspection
  checklist, including the `DEMO_MODE` flag. Edit this, not
  `Mine_Ute_Inspection_Checklist.html`.
- `build.py` — run after editing any `*_source.html` file to regenerate
  the deployable output files (embeds the logo and pixel font as base64
  into each page listed in its `PAGES` list): `python build.py`
- `index.html` / `Mine_Ute_Inspection_Checklist.html` — generated
  outputs, these are the files to deploy/host. Do not hand-edit
  (overwritten on build).
- `make_icons.py` — regenerates `icon-192.png` / `icon-512.png` from
  the logo.
- `manifest.json` — PWA config (name, colours, icons, `start_url`).
- `press-start-2p.woff2` — pixel display font, embedded by `build.py`.
- `Screenshot 2026-06-21 082454.png` — TJC logo, source for the
  embedded header image and app icons.
- `jspdf.umd.min.js` — jsPDF 2.5.1, bundled locally so PDF generation
  (in the real build) works offline.
- `sw.js` — service worker caching the app shell for offline use.

## What's deliberately left out of this repo

Compared to the live client project, this copy has no
`netlify/functions/` directory and no `netlify.toml` — there's no
serverless function here at all, since demo mode never calls it. There's
also no client `.docx` or working reference screenshots — just the app
itself.

## Installing on a phone

Same platform-aware install banner as the real build: a real one-tap
"Install" button on Chrome/Android (via `beforeinstallprompt`), an
expandable step-by-step guide on iOS Safari and browsers that don't
support one-tap install, and a warning to open the link in a real
browser first if it arrived via Messenger/WhatsApp (in-app browsers
can't add to the home screen at all).

## How the form works

- 5-step wizard: Job Details, then one step per checklist section
  (Lighting, Communication & Electrical, Vehicle Operation, Harness &
  Wiring).
- Each item is Pass / Fail / N/A. Selecting Fail opens a mandatory
  comment box for that item.
- One item, **Charge rate within specification**, is special: selecting
  Pass opens a mandatory number field instead ("volts"), shown in a blue
  info box rather than a defect.
- Final step shows a live "Summary of Comments" listing every failed
  item.
- Final screen ("Thanks Legend!") has a looping night-scene animation —
  a Grinch gets abducted by a UFO, then a cat makes a break for the
  bushes — followed by an honest note that this is demo mode and nothing
  was actually sent.
- Append `#preview-success` to the URL to jump straight to that final
  screen without filling out the form.

## Hosting

Deploy the same way as any static site: run `python build.py`, then
drag `index.html`, `Mine_Ute_Inspection_Checklist.html`, `manifest.json`,
`icon-192.png`, `icon-512.png`, `jspdf.umd.min.js`, and `sw.js` into
Netlify Drop (or any static host). No environment variables, no
serverless function, no email service needed — demo mode means there's
nothing to configure.
