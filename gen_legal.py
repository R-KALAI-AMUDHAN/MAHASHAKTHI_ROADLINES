import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

privacy_body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Privacy Policy</div>
      <span class="eyebrow">Legal</span>
      <h1>Privacy Policy</h1>
      <p>Last updated: September 2026</p>
    </div>
  </section>

  <section class="section">
    <div class="container legal-body">
      <p>This Privacy Policy explains how Mahashakthi Roadlines ("we", "us", "our") handles information collected through this website.</p>

      <h2>Information we collect</h2>
      <p>When you use the Request a Quote form, we ask for information such as your name, company name, mobile number, email address, pickup and delivery locations, and details about the goods to be transported. This information is provided voluntarily by you.</p>

      <h2>How we use information</h2>
      <p>Information submitted through this website is used solely to respond to your enquiry and, where relevant, to arrange the transportation service you have requested. We do not sell or rent your information to third parties.</p>

      <h2>Contacting you</h2>
      <p>We may contact you by phone, WhatsApp or email using the details you provide, in order to follow up on your enquiry.</p>

      <h2>Third-party services</h2>
      <p>This website uses Google Maps to display our office location and WhatsApp to allow you to message us directly. These services are operated by their respective providers, and your use of them is subject to their own privacy policies.</p>

      <h2>Data security</h2>
      <p>We take reasonable steps to protect information shared with us. However, no method of transmission over the internet is completely secure, and we cannot guarantee absolute security.</p>

      <h2>Cookies</h2>
      <p>This website does not currently use tracking cookies or third-party analytics beyond what is required to embed the Google Maps location on the Contact page.</p>

      <h2>Changes to this policy</h2>
      <p>We may update this Privacy Policy from time to time. Any changes will be reflected on this page.</p>

      <h2>Contact us</h2>
      <p>If you have questions about this Privacy Policy, please contact us at <a href="mailto:mahasakthiroadlines@gmail.com">mahasakthiroadlines@gmail.com</a> or call +91 96770 79089.</p>
    </div>
  </section>
'''

terms_body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Terms &amp; Conditions</div>
      <span class="eyebrow">Legal</span>
      <h1>Terms &amp; Conditions</h1>
      <p>Last updated: September 2026</p>
    </div>
  </section>

  <section class="section">
    <div class="container legal-body">
      <p>These Terms &amp; Conditions govern your use of this website and any enquiry submitted to Mahashakthi Roadlines through it. By using this website, you agree to these terms.</p>

      <h2>About this website</h2>
      <p>This website provides information about the road transportation, warehousing and logistics services offered by Mahashakthi Roadlines, operating from Madhavaram, Chennai. Content on this website is for general informational purposes.</p>

      <h2>Quotes and bookings</h2>
      <p>Submitting the Request a Quote form is an enquiry, not a confirmed booking. Vehicle availability, pricing and transportation timelines are confirmed directly with you by phone, WhatsApp or email following your enquiry.</p>

      <h2>Accuracy of information</h2>
      <p>We aim to keep the information on this website accurate and up to date, including details about our fleet, services and service areas. However, actual availability of vehicles and services is subject to confirmation at the time of your enquiry.</p>

      <h2>No liability for third-party services</h2>
      <p>This website links to third-party services such as Google Maps and WhatsApp. We are not responsible for the content, availability or practices of these third-party services.</p>

      <h2>Limitation of liability</h2>
      <p>Mahashakthi Roadlines will not be liable for any indirect or consequential loss arising from the use of this website. Terms specific to a confirmed transportation booking, including liability for goods in transit, will be agreed separately at the time of booking.</p>

      <h2>Governing law</h2>
      <p>These terms are governed by the laws of India, and any disputes will be subject to the jurisdiction of the courts in Chennai, Tamil Nadu.</p>

      <h2>Changes to these terms</h2>
      <p>We may update these Terms &amp; Conditions from time to time. Continued use of this website after changes are posted constitutes acceptance of the updated terms.</p>

      <h2>Contact us</h2>
      <p>For questions about these Terms &amp; Conditions, contact us at <a href="mailto:mahasakthiroadlines@gmail.com">mahasakthiroadlines@gmail.com</a> or call +91 96770 79089.</p>
    </div>
  </section>
'''

for fname, title, desc, body in [
    ("privacy.html", "Privacy Policy | Mahashakthi Roadlines",
     "Privacy Policy for the Mahashakthi Roadlines website, covering how enquiry information is collected and used.", privacy_body),
    ("terms.html", "Terms & Conditions | Mahashakthi Roadlines",
     "Terms & Conditions for using the Mahashakthi Roadlines website and submitting transportation enquiries.", terms_body),
]:
    html = page(title=title, description=desc, active="", body=body, canonical=fname)
    with open("/home/claude/mahashakthi/" + fname, "w") as f:
        f.write(html)
    print(fname, "written", len(html))
