import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page, route_rule_svg

ROUTE = route_rule_svg()

body = '''
  <!-- HERO -->
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-copy reveal">
        <span class="hero-badge"><span class="dot"></span>Serving businesses since 2013</span>
        <h1>Reliable road transportation.<br>Connecting businesses across India.</h1>
        <p class="lead">Mahashakthi Roadlines provides dependable goods transportation, warehousing and logistics solutions designed to move your business forward.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="quote.html">Request a Quote</a>
          <a class="btn btn-outline-light" href="contact.html">Talk to Us</a>
        </div>
      </div>
      <div class="hero-visual reveal">
        <div class="route-panel">
          <div class="route-panel-title">MAHASHAKTHI ROADLINES AT A GLANCE</div>
          <div class="route-track">
            <div class="route-stop"><div class="fig">2013</div><div class="lbl">Company established</div></div>
            <div class="route-stop"><div class="fig">20+</div><div class="lbl">Vehicles available across categories</div></div>
            <div class="route-stop"><div class="fig">1</div><div class="lbl">Head office &mdash; Madhavaram, Chennai</div></div>
            <div class="route-stop"><div class="fig">Pan-India</div><div class="lbl">Road transportation reach</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- STATS STRIP -->
  <section class="stats-strip">
    <div class="container stats-row">
      <div class="stat-cell reveal"><div class="stat-fig"><span data-count-to="2013">0</span></div><div class="stat-lbl">Established</div></div>
      <div class="stat-cell reveal"><div class="stat-fig"><span data-count-to="20" data-count-suffix="+">0</span></div><div class="stat-lbl">Fleet &amp; vehicle availability</div></div>
      <div class="stat-cell reveal"><div class="stat-fig"><span data-count-to="1">0</span></div><div class="stat-lbl">Branch &mdash; Madhavaram, Chennai</div></div>
      <div class="stat-cell reveal"><div class="stat-fig">Pan-India</div><div class="stat-lbl">Logistics reach</div></div>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What we do</span>
        <h2>Our transportation &amp; logistics services</h2>
        <p>From individual consignments to large-scale transportation requirements, we arrange road transportation solutions based on cargo, destination and vehicle requirements.</p>
      </div>
      <div class="grid grid-3">
        <div class="service-card reveal">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="1" y="7" width="14" height="10" rx="1"/><path d="M15 10h4l3 3v4h-7z"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="19" r="2"/></svg>
          <h3>Goods Transportation</h3>
          <p>Reliable road transportation for different types of cargo, arranged around your pickup and delivery requirements.</p>
          <a class="card-link" href="services.html">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
        <div class="service-card reveal">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 9.5 12 4l9 5.5V19a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M8 20v-7h8v7"/></svg>
          <h3>Warehousing</h3>
          <p>Storage and handling solutions that support supply-chain requirements alongside road transportation.</p>
          <a class="card-link" href="services.html">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
        <div class="service-card reveal">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/></svg>
          <h3>Logistics Solutions</h3>
          <p>Transportation and logistics support tailored to business requirements, from single shipments to recurring cargo.</p>
          <a class="card-link" href="services.html">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
        <div class="service-card reveal">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 17h2l1-5h10l1 5h2"/><path d="M7 12 9 6h6l2 6"/><circle cx="8" cy="19" r="1.6"/><circle cx="16" cy="19" r="1.6"/></svg>
          <h3>Road Freight</h3>
          <p>Efficient road-based movement of goods across destinations in India, using vehicles suited to the load.</p>
          <a class="card-link" href="services.html">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
        <div class="service-card reveal">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="8" width="20" height="9" rx="1"/><path d="M2 12h20M8 8v9M16 8v9"/></svg>
          <h3>Full / Dedicated Vehicle Solutions</h3>
          <p>Vehicle arrangements based on cargo requirements, giving a dedicated vehicle for your consignment.</p>
          <a class="card-link" href="services.html">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
        <div class="service-card reveal">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h16v6H4zM4 14h10v6H4zM17 14h3v6h-3z"/></svg>
          <h3>Customized Transport Solutions</h3>
          <p>Flexible transportation arrangements depending on cargo type, quantity and destination.</p>
          <a class="card-link" href="services.html">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </div>
    </div>
  </section>

  <!-- WHY CHOOSE US -->
  <section class="section section--alt">
    <div class="container grid grid-2" style="align-items:start;gap:56px;">
      <div class="reveal">
        <span class="eyebrow">Why Mahashakthi Roadlines</span>
        <h2>Why businesses choose us</h2>
        <p>A straightforward approach to road transportation, built on availability and follow-through rather than promises.</p>
      </div>
      <div class="reveal">
        <div class="reason-row">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/></svg>
          <div><h3>Experience since 2013</h3><p>Operating in road transportation and logistics from Madhavaram, Chennai.</p></div>
        </div>
        <div class="reason-row">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="1" y="7" width="14" height="10" rx="1"/><path d="M15 10h4l3 3v4h-7z"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="19" r="2"/></svg>
          <div><h3>Flexible vehicle availability</h3><p>Vehicles arranged from our fleet based on the size and nature of your cargo.</p></div>
        </div>
        <div class="reason-row">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4h16v6H4zM4 14h10v6H4zM17 14h3v6h-3z"/></svg>
          <div><h3>Multiple cargo requirements</h3><p>Support for a range of goods and consignment types across industries.</p></div>
        </div>
        <div class="reason-row">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 12 9 6h6l2 6"/><path d="M4 17h2l1-5h10l1 5h2"/><circle cx="8" cy="19" r="1.6"/><circle cx="16" cy="19" r="1.6"/></svg>
          <div><h3>Road transportation expertise</h3><p>Focused on roadways, with vehicle types suited to different routes and loads.</p></div>
        </div>
        <div class="reason-row">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 9.5 12 4l9 5.5V19a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M8 20v-7h8v7"/></svg>
          <div><h3>Warehousing support</h3><p>Storage and handling solutions alongside transportation, where required.</p></div>
        </div>
        <div class="reason-row">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4v16h16"/><path d="M8 15l3-4 3 3 4-6"/></svg>
          <div><h3>Customer-focused service</h3><p>Requirements discussed directly, with vehicle and route arranged accordingly.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Process</span>
        <h2>How it works</h2>
        <p>A straightforward four-step process from enquiry to delivery.</p>
      </div>
      <div class="process-track reveal">
        <div class="process-step"><div class="num">1</div><h3>Share your requirement</h3><p>Tell us what needs to move, the pickup and delivery locations, and the timeline.</p></div>
        <div class="process-step"><div class="num">2</div><h3>Get a transport solution</h3><p>We match your cargo to a suitable vehicle from our fleet and confirm the arrangement.</p></div>
        <div class="process-step"><div class="num">3</div><h3>Goods pickup</h3><p>The assigned vehicle arrives at the pickup location to load your consignment.</p></div>
        <div class="process-step"><div class="num">4</div><h3>Safe delivery</h3><p>Your goods are transported by road to the delivery destination.</p></div>
      </div>
    </div>
  </section>

  <!-- NETWORK PREVIEW -->
  <section class="section section--alt">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Reach</span>
        <h2>Moving goods across India</h2>
        <p>Mahashakthi Roadlines provides road-based logistics and transportation support across India, operating from our head office in Madhavaram, Chennai.</p>
      </div>
      <div class="reveal">
        <a class="btn btn-outline" href="network.html">View our network &amp; service areas</a>
      </div>
    </div>
  </section>

  <!-- INDUSTRIES -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Who we serve</span>
        <h2>Industries we serve</h2>
        <p>General cargo and sector-specific transportation requirements, supported as they come in.</p>
      </div>
      <div class="industry-grid reveal">
        <div class="industry-cell"><h3>Manufacturing</h3></div>
        <div class="industry-cell"><h3>Automotive</h3></div>
        <div class="industry-cell"><h3>FMCG</h3></div>
        <div class="industry-cell"><h3>Retail</h3></div>
        <div class="industry-cell"><h3>Construction</h3></div>
        <div class="industry-cell"><h3>Industrial Goods</h3></div>
        <div class="industry-cell"><h3>Agriculture</h3></div>
        <div class="industry-cell"><h3>General Cargo</h3></div>
        <div class="industry-cell"><h3>E-Commerce &amp; Distribution</h3></div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Need a reliable transportation partner?</h2>
          <p>Tell us what you need to move, where it needs to go, and when you need it.</p>
        </div>
        <div class="cta-band-actions">
          <a class="btn btn-primary" href="quote.html">Request a Quote</a>
          <a class="btn btn-outline-light" href="tel:+919677079089">Call Us</a>
          <a class="btn btn-outline-light" data-wa-link href="#">WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="Mahashakthi Roadlines | Transportation & Logistics Company in Chennai",
    description="Mahashakthi Roadlines provides goods transportation, warehousing and logistics solutions from Madhavaram, Chennai, serving transportation requirements across India.",
    active="index.html",
    body=body,
    canonical="",
)
with open("/home/claude/mahashakthi/index.html", "w") as f:
    f.write(html)
print("index.html written", len(html))
