# Generates all HTML pages for the Mahashakthi Roadlines site
# from shared header/footer partials + per-page content.
import os

ROOT = "/home/claude/mahashakthi"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("services.html", "Services"),
    ("fleet.html", "Fleet"),
    ("network.html", "Network"),
    ("industries.html", "Industries"),
]

SVG_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.34 1.79.65 2.65a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.43-1.43a2 2 0 0 1 2.11-.45c.86.31 1.75.53 2.65.65A2 2 0 0 1 22 16.92z"/></svg>'
SVG_WHATSAPP = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.44 1.32 4.94L2 22l5.24-1.37c1.44.79 3.06 1.2 4.8 1.2h.01c5.5 0 9.96-4.46 9.96-9.96S17.55 2 12.04 2zm5.86 14.1c-.25.7-1.45 1.34-2 1.43-.53.08-1.2.11-1.94-.12-.45-.14-1.02-.33-1.76-.64-3.1-1.34-5.12-4.46-5.28-4.67-.16-.21-1.26-1.68-1.26-3.2s.79-2.28 1.07-2.59c.28-.31.6-.38.8-.38.2 0 .4 0 .58.01.19.01.44-.07.68.53.25.6.85 2.08.92 2.23.08.16.13.34.02.55-.1.21-.16.34-.31.52-.16.18-.33.4-.47.54-.16.16-.32.33-.14.64.19.31.83 1.37 1.78 2.22 1.22 1.09 2.25 1.43 2.56 1.59.31.16.49.13.67-.08.19-.21.79-.92 1-1.24.21-.31.42-.26.7-.16.29.1 1.83.86 2.15 1.02.31.16.52.23.6.36.08.13.08.75-.17 1.45z"/></svg>'
SVG_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
SVG_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg>'

def route_rule_svg():
    return ('<svg viewBox="0 0 1000 20" preserveAspectRatio="none">'
            '<line x1="0" y1="10" x2="1000" y2="10" stroke="#DFE2E8" stroke-width="2" stroke-dasharray="2 10" stroke-linecap="round"/>'
            '<circle cx="10" cy="10" r="5" fill="#C41E2E"/>'
            '</svg>')

def header(active, depth=""):
    nav_links = "\n        ".join(
        '<a href="{0}{1}"{2}>{3}</a>'.format(depth, href, ' class="active"' if href == active else '', label)
        for href, label in NAV_ITEMS
    )
    mobile_links = "\n        ".join(
        '<a href="{0}{1}"{2}>{3}</a>'.format(depth, href, ' class="active"' if href == active else '', label)
        for href, label in NAV_ITEMS
    )
    return '''  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{depth}index.html" aria-label="Mahashakthi Roadlines — Home">
        <img src="{depth}assets/logo-300.png" alt="Mahashakthi Roadlines logo" width="160" height="110">
      </a>
      <nav class="main-nav" aria-label="Primary">
        {nav_links}
      </nav>
      <div class="header-actions">
        <a class="icon-btn call-desktop" href="tel:+919677079089" aria-label="Call Mahashakthi Roadlines">{phone_icon}</a>
        <a class="icon-btn whatsapp" data-wa-link href="#" aria-label="Chat on WhatsApp">{wa_icon}</a>
        <a class="btn btn-primary" href="{depth}quote.html">Request a Quote</a>
        <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">{menu_icon}</button>
      </div>
    </div>
  </header>

  <div class="mobile-nav" role="dialog" aria-label="Mobile menu">
    <div class="container">
      <div style="display:flex;justify-content:flex-end;padding:8px 0 4px;">
        <button class="nav-toggle" aria-label="Close menu">{close_icon}</button>
      </div>
      <nav aria-label="Mobile primary">
        {mobile_links}
      </nav>
      <div class="mobile-nav-contact">
        <a class="btn btn-primary btn-block" href="{depth}quote.html">Request a Quote</a>
        <a class="btn btn-outline btn-block" href="tel:+919677079089">{phone_icon} Call +91 96770 79089</a>
        <a class="btn btn-outline btn-block" data-wa-link href="#">{wa_icon} WhatsApp Us</a>
      </div>
    </div>
  </div>
'''.format(depth=depth, nav_links=nav_links, mobile_links=mobile_links,
           phone_icon=SVG_PHONE, wa_icon=SVG_WHATSAPP, menu_icon=SVG_MENU, close_icon=SVG_CLOSE)

def footer(depth=""):
    return '''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="{depth}assets/logo-300.png" alt="Mahashakthi Roadlines logo" width="140" height="96">
          <p>Road transportation, warehousing and logistics services operating from Madhavaram, Chennai since 2013.</p>
          <div class="footer-social" aria-label="Social media (accounts to be added)">
            <a href="#" aria-label="Instagram (coming soon)" tabindex="-1" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/></svg></a>
            <a href="#" aria-label="Facebook (coming soon)" tabindex="-1" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M14 9h3V6h-3c-1.66 0-3 1.34-3 3v2H8v3h3v7h3v-7h3l1-3h-4V9c0-.55.45-1 1-1z"/></svg></a>
            <a href="#" aria-label="LinkedIn (coming soon)" tabindex="-1" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="7" y1="10" x2="7" y2="16"/><circle cx="7" cy="7" r="0.6" fill="currentColor"/><path d="M11 16v-4a2 2 0 0 1 4 0v4"/><line x1="11" y1="10" x2="11" y2="16"/></svg></a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="{depth}index.html">Home</a></li>
            <li><a href="{depth}about.html">About Us</a></li>
            <li><a href="{depth}services.html">Services</a></li>
            <li><a href="{depth}fleet.html">Fleet</a></li>
            <li><a href="{depth}network.html">Network</a></li>
            <li><a href="{depth}quote.html">Request a Quote</a></li>
            <li><a href="{depth}contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="{depth}services.html">Goods Transportation</a></li>
            <li><a href="{depth}services.html">Warehousing</a></li>
            <li><a href="{depth}services.html">Logistics Support</a></li>
            <li><a href="{depth}services.html">Road Freight</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:+919677079089">+91 96770 79089</a></li>
            <li><a data-wa-link href="#">WhatsApp: +91 96770 79089</a></li>
            <li><a href="mailto:mahasakthiroadlines@gmail.com">mahasakthiroadlines@gmail.com</a></li>
            <li>No. 70, 2nd Cross Street, Anna Street, Madhavaram, Chennai&nbsp;600060, Tamil Nadu, India</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Mahashakthi Roadlines. All rights reserved.</span>
        <span class="footer-bottom-links">
          <a href="{depth}privacy.html">Privacy Policy</a>
          <a href="{depth}terms.html">Terms &amp; Conditions</a>
        </span>
      </div>
    </div>
  </footer>

  <a class="wa-float" data-wa-link href="#" aria-label="Chat on WhatsApp">{wa_icon}</a>

  <div class="mobile-action-bar">
    <div class="row">
      <a href="tel:+919677079089">{phone_icon}<span>Call</span></a>
      <a data-wa-link href="#">{wa_icon}<span>WhatsApp</span></a>
      <a href="{depth}quote.html"><span>Get a Quote</span></a>
    </div>
  </div>

  <script src="{depth}js/main.js"></script>
'''.format(depth=depth, wa_icon=SVG_WHATSAPP, phone_icon=SVG_PHONE)

def page(title, description, active, body, canonical, extra_head="", depth=""):
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.mahashakthiroadlines.com/{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.mahashakthiroadlines.com/assets/logo-600.png">
<meta property="og:url" content="https://www.mahashakthiroadlines.com/{canonical}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/png" href="{depth}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{depth}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}css/style.css">
{extra_head}</head>
<body>
{header}
{body}
{footer}
</body>
</html>
'''.format(title=title, description=description, canonical=canonical, depth=depth,
           extra_head=extra_head, header=header(active, depth), body=body, footer=footer(depth))

print("build.py loaded")
