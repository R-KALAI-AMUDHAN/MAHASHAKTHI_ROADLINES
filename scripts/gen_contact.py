import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Contact Us</div>
      <span class="eyebrow">Contact us</span>
      <h1>Get in touch</h1>
      <p>Reach us by phone, WhatsApp or email, or visit our head office in Madhavaram, Chennai.</p>
    </div>
  </section>

  <section class="section">
    <div class="container contact-grid">
      <div class="reveal">
        <h2 style="font-size:1.4rem;">Mahashakthi Roadlines</h2>
        <div class="contact-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s7-6.5 7-11.5A7 7 0 0 0 5 9.5C5 14.5 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.4"/></svg>
          <div><h3>Head office</h3><p>No. 70, 2nd Cross Street,<br>Anna Street, Madhavaram,<br>Chennai &ndash; 600060,<br>Tamil Nadu, India.</p></div>
        </div>
        <div class="contact-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.34 1.79.65 2.65a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.43-1.43a2 2 0 0 1 2.11-.45c.86.31 1.75.53 2.65.65A2 2 0 0 1 22 16.92z"/></svg>
          <div><h3>Phone</h3><p><a href="tel:+919677079089">+91 96770 79089</a></p></div>
        </div>
        <div class="contact-item">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.44 1.32 4.94L2 22l5.24-1.37c1.44.79 3.06 1.2 4.8 1.2h.01c5.5 0 9.96-4.46 9.96-9.96S17.55 2 12.04 2zm5.86 14.1c-.25.7-1.45 1.34-2 1.43-.53.08-1.2.11-1.94-.12-.45-.14-1.02-.33-1.76-.64-3.1-1.34-5.12-4.46-5.28-4.67-.16-.21-1.26-1.68-1.26-3.2s.79-2.28 1.07-2.59c.28-.31.6-.38.8-.38.2 0 .4 0 .58.01.19.01.44-.07.68.53.25.6.85 2.08.92 2.23.08.16.13.34.02.55-.1.21-.16.34-.31.52-.16.18-.33.4-.47.54-.16.16-.32.33-.14.64.19.31.83 1.37 1.78 2.22 1.22 1.09 2.25 1.43 2.56 1.59.31.16.49.13.67-.08.19-.21.79-.92 1-1.24.21-.31.42-.26.7-.16.29.1 1.83.86 2.15 1.02.31.16.52.23.6.36.08.13.08.75-.17 1.45z"/></svg>
          <div><h3>WhatsApp</h3><p><a data-wa-link href="#">+91 96770 79089</a></p></div>
        </div>
        <div class="contact-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 6l10 7 10-7"/></svg>
          <div><h3>Email</h3><p><a href="mailto:mahasakthiroadlines@gmail.com">mahasakthiroadlines@gmail.com</a></p></div>
        </div>
        <div class="hero-ctas" style="margin-top:24px;">
          <a class="btn btn-primary" href="tel:+919677079089">Call Now</a>
          <a class="btn btn-outline" data-wa-link href="#">WhatsApp</a>
          <a class="btn btn-outline" href="mailto:mahasakthiroadlines@gmail.com">Email Us</a>
          <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&query=No.+70%2C+2nd+Cross+Street%2C+Anna+Street%2C+Madhavaram%2C+Chennai+600060" target="_blank" rel="noopener">Get Directions</a>
        </div>
      </div>
      <div class="reveal">
        <div class="map-embed">
          <iframe
            src="https://www.google.com/maps?q=No.+70,+2nd+Cross+Street,+Anna+Street,+Madhavaram,+Chennai+600060,+Tamil+Nadu,+India&output=embed"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            title="Mahashakthi Roadlines head office location on Google Maps"
            allowfullscreen>
          </iframe>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Have a transportation requirement?</h2>
          <p>Request a quote and we'll match you with the right vehicle for the job.</p>
        </div>
        <div class="cta-band-actions">
          <a class="btn btn-primary" href="quote.html">Request a Quote</a>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="Contact Us | Mahashakthi Roadlines",
    description="Contact Mahashakthi Roadlines in Madhavaram, Chennai by phone, WhatsApp or email, or find directions to our head office.",
    active="",
    body=body,
    canonical="contact.html",
)
with open("/home/claude/mahashakthi/contact.html", "w") as f:
    f.write(html)
print("contact.html written", len(html))
