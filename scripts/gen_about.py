import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / About Us</div>
      <span class="eyebrow">About us</span>
      <h1>About Mahashakthi Roadlines</h1>
      <p>A road transportation, warehousing and logistics company operating from Madhavaram, Chennai since 2013.</p>
    </div>
  </section>

  <section class="section">
    <div class="container grid grid-2" style="gap:56px;">
      <div class="reveal">
        <span class="eyebrow">Company overview</span>
        <h2>Built on road transportation experience</h2>
        <p>Mahashakthi Roadlines was established on 18 February 2013 under the leadership of K. Rajeshbabu. The company operates from Madhavaram, Chennai and provides road transportation, warehousing and logistics services.</p>
        <p>We focus on reliable transportation solutions for different types of goods and customer requirements, using a fleet of approximately 20 vehicles arranged according to the cargo, route and vehicle needed for each consignment.</p>
        <p>All transportation is carried out by road, across destinations in India, from our head office in Madhavaram.</p>
      </div>
      <div class="reveal">
        <div class="timeline">
          <div class="timeline-item"><div class="yr">2013</div><p>Company established under the leadership of K. Rajeshbabu, Madhavaram, Chennai.</p></div>
          <div class="timeline-item"><div class="yr">Present</div><p>Transportation, warehousing and logistics operations, serving requirements across India by road.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="grid grid-2" style="gap:40px;">
        <div class="reveal">
          <span class="eyebrow">Our mission</span>
          <h2>Mission</h2>
          <p>To provide dependable road transportation, warehousing and logistics solutions that move our customers' goods safely and on schedule, arranged around each customer's specific requirements.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow">Our vision</span>
          <h2>Vision</h2>
          <p>To grow as a trusted road transportation partner for businesses across India, known for reliability and straightforward customer service.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What guides us</span>
        <h2>Our values</h2>
      </div>
      <div class="value-list reveal">
        <div class="value-item"><h3>Reliability</h3><p>Doing what we say, from pickup to delivery.</p></div>
        <div class="value-item"><h3>Safety</h3><p>Careful handling and transportation of every consignment.</p></div>
        <div class="value-item"><h3>Customer Commitment</h3><p>Understanding each requirement before arranging a solution.</p></div>
        <div class="value-item"><h3>Flexibility</h3><p>Vehicle and route arrangements suited to the cargo at hand.</p></div>
        <div class="value-item"><h3>Professionalism</h3><p>Clear communication throughout the transportation process.</p></div>
        <div class="value-item"><h3>Timely Service</h3><p>Respecting the schedules our customers depend on.</p></div>
      </div>
    </div>
  </section>

  <section class="section section--navy">
    <div class="container">
      <div class="cta-band reveal" style="background:var(--navy-800);">
        <div>
          <h2>Want to know more about our services?</h2>
          <p>Get in touch and tell us about your transportation requirement.</p>
        </div>
        <div class="cta-band-actions">
          <a class="btn btn-primary" href="quote.html">Request a Quote</a>
          <a class="btn btn-outline-light" href="contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="About Us | Mahashakthi Roadlines",
    description="Mahashakthi Roadlines was established on 18 February 2013 under K. Rajeshbabu, operating road transportation, warehousing and logistics services from Madhavaram, Chennai.",
    active="about.html",
    body=body,
    canonical="about.html",
)
with open("/home/claude/mahashakthi/about.html", "w") as f:
    f.write(html)
print("about.html written", len(html))
