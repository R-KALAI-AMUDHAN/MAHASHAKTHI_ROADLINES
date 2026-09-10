# Mahashakthi Roadlines — Website

A static, dependency-free website (HTML/CSS/JS — no build step required).

## Structure
```
index.html          Home
about.html           About Us
services.html        Services
fleet.html           Our Fleet
network.html         Network / Service Areas
industries.html      Industries We Serve
quote.html           Request a Quote (form)
contact.html         Contact Us (with Google Maps embed)
privacy.html         Privacy Policy
terms.html           Terms & Conditions
css/style.css        Shared design system
js/main.js           Shared behaviour (nav, WhatsApp links, form, animations)
assets/              Logo files + favicons (generated from the provided logo)
robots.txt, sitemap.xml
```

## Running it
No build tools needed. Open `index.html` in a browser, or serve the folder
with any static file server, e.g.:
```
python3 -m http.server 8000
```
Then visit http://localhost:8000

## What's real vs. placeholder
- All copy uses only the facts provided: est. 18 Feb 2013, K. Rajeshbabu,
  Madhavaram Chennai head office, ~20 vehicles, 1 branch, roadways-only,
  pan-India reach. No invented stats, clients, awards or certifications.
- The "Fleet" page uses simple line-icon illustrations for vehicle
  categories, not stock photos, since no real fleet photographs exist yet.
  Swap in real photos later — just replace the `<div class="art">...</div>`
  contents in `fleet.html`.
- The "Network" page uses an abstract service-reach diagram (not a literal
  India map), so it never implies branch offices that don't exist.
- Social media icons in the footer are inert placeholders (no accounts
  exist yet) — add real links in every page's footer once accounts exist,
  or better, extract the footer into a templating step if the site grows.
- The Request a Quote form validates in the browser but has **no backend**.
  It currently just shows a success message locally. To actually receive
  submissions, connect `js/main.js`'s `initQuoteForm` submit handler to:
  - an email API (e.g. Formspree, EmailJS, or a small backend endpoint), or
  - a Google Sheet / CRM via a serverless function.
- Shipment tracking, customer portal, admin dashboard and driver/vehicle
  management are intentionally NOT built — the brief asked only that the
  site not block them later. No fake tracking UI has been added.

## Editing content
Each page is self-contained HTML (header/footer markup is duplicated per
page, not templated at runtime) so search engines and no-JS visitors see
full content immediately. If you regenerate pages, the Python scripts
(`build.py`, `gen_*.py`) used to build them are included for reference —
they are not needed to run the site.

## Before going live
- Replace the Google Maps `<iframe>` src on `contact.html` with an
  embed code pulled from Google Maps directly (search the address there,
  Share > Embed a map) for the most accurate marker placement.
- Update `https://www.mahashakthiroadlines.com/` in canonical/OG tags and
  `sitemap.xml`/`robots.txt` if the real domain differs.
- Add real fleet photographs, and real social media links, when available.
