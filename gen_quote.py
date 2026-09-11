import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Request a Quote</div>
      <span class="eyebrow">Request a quote</span>
      <h1>Tell us what you need to move</h1>
      <p>Share your pickup, delivery and cargo details and we will get back to you with a suitable transportation solution.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-2" style="gap:48px;align-items:start;">
        <div class="form-card reveal">
          <form id="quote-form" novalidate>
            <div class="form-grid">
              <div class="field">
                <label for="q-name">Full Name <span class="req">*</span></label>
                <input type="text" id="q-name" name="fullName" required autocomplete="name">
                <div class="error-msg">Please enter your name.</div>
              </div>
              <div class="field">
                <label for="q-company">Company Name</label>
                <input type="text" id="q-company" name="companyName" autocomplete="organization">
              </div>
              <div class="field">
                <label for="quote-phone">Mobile Number <span class="req">*</span></label>
                <input type="tel" id="quote-phone" name="mobileNumber" required autocomplete="tel" inputmode="tel">
                <div class="error-msg">Please enter a valid mobile number.</div>
              </div>
              <div class="field">
                <label for="quote-email">Email</label>
                <input type="email" id="quote-email" name="email" autocomplete="email">
                <div class="error-msg">Please enter a valid email address.</div>
              </div>
              <div class="field">
                <label for="q-pickup">Pickup Location <span class="req">*</span></label>
                <input type="text" id="q-pickup" name="pickupLocation" required>
                <div class="error-msg">Please enter the pickup location.</div>
              </div>
              <div class="field">
                <label for="q-delivery">Delivery Location <span class="req">*</span></label>
                <input type="text" id="q-delivery" name="deliveryLocation" required>
                <div class="error-msg">Please enter the delivery location.</div>
              </div>
              <div class="field">
                <label for="q-goods">Type of Goods <span class="req">*</span></label>
                <input type="text" id="q-goods" name="typeOfGoods" required>
                <div class="error-msg">Please describe the type of goods.</div>
              </div>
              <div class="field">
                <label for="q-weight">Approximate Weight</label>
                <input type="text" id="q-weight" name="approxWeight" placeholder="e.g. 5 tonnes">
              </div>
              <div class="field">
                <label for="q-qty">Approximate Quantity</label>
                <input type="text" id="q-qty" name="approxQuantity" placeholder="e.g. 200 boxes">
              </div>
              <div class="field">
                <label for="q-vehicle">Vehicle Requirement</label>
                <select id="q-vehicle" name="vehicleRequirement">
                  <option value="">Not sure / please advise</option>
                  <option>Light Commercial Vehicle</option>
                  <option>Medium Goods Vehicle</option>
                  <option>Heavy Goods Vehicle</option>
                  <option>Large Capacity Vehicle</option>
                  <option>Specialized Vehicle</option>
                </select>
              </div>
              <div class="field">
                <label for="q-date">Preferred Pickup Date</label>
                <input type="date" id="q-date" name="preferredPickupDate">
              </div>
              <div class="field full">
                <label for="q-message">Additional Requirements / Message</label>
                <textarea id="q-message" name="message" placeholder="Any other details we should know"></textarea>
              </div>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Request a Quote</button>
            <p class="form-note text-center" style="margin-top:14px;">Fields marked <span class="req">*</span> are required. We typically respond by phone or WhatsApp.</p>
          </form>

          <div class="form-success" id="quote-success">
            <div class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 13l4 4L19 7"/></svg></div>
            <h2>Request received</h2>
            <p>Thank you for sharing your requirement. Our team will get back to you shortly on the mobile number provided.</p>
            <div class="hero-ctas" style="justify-content:center;">
              <a class="btn btn-outline" href="tel:+919677079089">Call Us</a>
              <a class="btn btn-primary" data-wa-link data-wa-message="Hello MAHASHAKTHI ROADLINES, I just submitted a quote request on your website." href="#">WhatsApp Us</a>
            </div>
          </div>
        </div>

        <div class="reveal">
          <div class="notice" style="margin-bottom:24px;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg>
            <span>This form does not send an email automatically yet &mdash; no backend or email service is connected. For an immediate response, please call or WhatsApp us directly.</span>
          </div>
          <h3>Prefer to talk directly?</h3>
          <div class="contact-item">
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.34 1.79.65 2.65a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.43-1.43a2 2 0 0 1 2.11-.45c.86.31 1.75.53 2.65.65A2 2 0 0 1 22 16.92z"/></svg>
            <div><h3>Call</h3><p><a href="tel:+919677079089">+91 96770 79089</a></p></div>
          </div>
          <div class="contact-item">
            <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.44 1.32 4.94L2 22l5.24-1.37c1.44.79 3.06 1.2 4.8 1.2h.01c5.5 0 9.96-4.46 9.96-9.96S17.55 2 12.04 2zm5.86 14.1c-.25.7-1.45 1.34-2 1.43-.53.08-1.2.11-1.94-.12-.45-.14-1.02-.33-1.76-.64-3.1-1.34-5.12-4.46-5.28-4.67-.16-.21-1.26-1.68-1.26-3.2s.79-2.28 1.07-2.59c.28-.31.6-.38.8-.38.2 0 .4 0 .58.01.19.01.44-.07.68.53.25.6.85 2.08.92 2.23.08.16.13.34.02.55-.1.21-.16.34-.31.52-.16.18-.33.4-.47.54-.16.16-.32.33-.14.64.19.31.83 1.37 1.78 2.22 1.22 1.09 2.25 1.43 2.56 1.59.31.16.49.13.67-.08.19-.21.79-.92 1-1.24.21-.31.42-.26.7-.16.29.1 1.83.86 2.15 1.02.31.16.52.23.6.36.08.13.08.75-.17 1.45z"/></svg>
            <div><h3>WhatsApp</h3><p><a data-wa-link href="#">+91 96770 79089</a></p></div>
          </div>
          <div class="contact-item">
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 6l10 7 10-7"/></svg>
            <div><h3>Email</h3><p><a href="mailto:mahasakthiroadlines@gmail.com">mahasakthiroadlines@gmail.com</a></p></div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="Request a Quote | Mahashakthi Roadlines",
    description="Request a transportation quote from Mahashakthi Roadlines. Share your pickup, delivery and cargo details and we will get back to you.",
    active="",
    body=body,
    canonical="quote.html",
)
with open("/home/claude/mahashakthi/quote.html", "w") as f:
    f.write(html)
print("quote.html written", len(html))
