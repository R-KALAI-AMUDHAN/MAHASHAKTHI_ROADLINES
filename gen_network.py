import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

# Abstract radial "service reach" diagram — deliberately not a literal
# map, so we never imply branch offices that don't exist. Hub = head
# office; spokes = broad directional regions we can serve by road.
reach_svg = """
<svg viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram of road transportation reach radiating from the Madhavaram, Chennai head office">
  <circle cx="320" cy="240" r="200" fill="none" stroke="#E3E6EA" stroke-width="1"/>
  <circle cx="320" cy="240" r="145" fill="none" stroke="#E3E6EA" stroke-width="1"/>
  <circle cx="320" cy="240" r="90" fill="none" stroke="#E3E6EA" stroke-width="1"/>
  <g stroke="#C41E2E" stroke-width="1.5" stroke-dasharray="2 8" stroke-linecap="round">
    <line x1="320" y1="240" x2="320" y2="55"/>
    <line x1="320" y1="240" x2="478" y2="145"/>
    <line x1="320" y1="240" x2="478" y2="335"/>
    <line x1="320" y1="240" x2="320" y2="425"/>
    <line x1="320" y1="240" x2="162" y2="335"/>
    <line x1="320" y1="240" x2="162" y2="145"/>
  </g>
  <circle cx="320" cy="240" r="34" fill="#0A1A31"/>
  <circle cx="320" cy="55" r="5" fill="#0A1A31"/>
  <circle cx="478" cy="145" r="5" fill="#0A1A31"/>
  <circle cx="478" cy="335" r="5" fill="#0A1A31"/>
  <circle cx="320" cy="425" r="5" fill="#0A1A31"/>
  <circle cx="162" cy="335" r="5" fill="#0A1A31"/>
  <circle cx="162" cy="145" r="5" fill="#0A1A31"/>
  <text x="320" y="236" text-anchor="middle" fill="#FFFFFF" font-family="Manrope, sans-serif" font-weight="800" font-size="11">HEAD</text>
  <text x="320" y="250" text-anchor="middle" fill="#FFFFFF" font-family="Manrope, sans-serif" font-weight="800" font-size="11">OFFICE</text>
  <text x="320" y="38" text-anchor="middle" fill="#4E5768" font-family="Inter, sans-serif" font-size="13" font-weight="600">North India</text>
  <text x="490" y="141" text-anchor="start" fill="#4E5768" font-family="Inter, sans-serif" font-size="13" font-weight="600">East India</text>
  <text x="490" y="339" text-anchor="start" fill="#4E5768" font-family="Inter, sans-serif" font-size="13" font-weight="600">South-East</text>
  <text x="320" y="452" text-anchor="middle" fill="#4E5768" font-family="Inter, sans-serif" font-size="13" font-weight="600">South India</text>
  <text x="150" y="339" text-anchor="end" fill="#4E5768" font-family="Inter, sans-serif" font-size="13" font-weight="600">South-West</text>
  <text x="150" y="141" text-anchor="end" fill="#4E5768" font-family="Inter, sans-serif" font-size="13" font-weight="600">West India</text>
</svg>
"""

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Network</div>
      <span class="eyebrow">Network &amp; service areas</span>
      <h1>Road transportation across India</h1>
      <p>Mahashakthi Roadlines provides road-based logistics and transportation support across India, operating from our head office in Madhavaram, Chennai.</p>
    </div>
  </section>

  <section class="section">
    <div class="container map-wrap">
      <div class="reveal">''' + reach_svg + '''
        <p class="form-note text-center">Illustrative diagram of road transportation reach from our head office. It does not represent branch offices or exact routes.</p>
      </div>
      <div class="reveal">
        <span class="eyebrow">Head office</span>
        <h2>Madhavaram, Chennai</h2>
        <p>All operations are coordinated from our head office at No. 70, 2nd Cross Street, Anna Street, Madhavaram, Chennai &ndash; 600060, Tamil Nadu. Mahashakthi Roadlines currently operates one branch.</p>
        <ul class="map-legend">
          <li><span class="swatch" style="background:var(--navy-900);"></span> Head office &mdash; Madhavaram, Chennai (1 branch)</li>
          <li><span class="swatch" style="background:var(--red-600);"></span> Road transportation reach across India</li>
        </ul>
        <p class="form-note">Service availability depends on cargo requirements, destination and vehicle availability at the time of booking.</p>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Coverage</span>
        <h2>How our service area works</h2>
        <p>We do not operate fixed branch offices beyond Madhavaram, Chennai. Road transportation to other parts of India is arranged per requirement.</p>
      </div>
      <div class="grid grid-3 reveal">
        <div class="service-card">
          <h3>Roadways only</h3>
          <p>All transportation is carried out by road, using vehicles suited to the destination and cargo.</p>
        </div>
        <div class="service-card">
          <h3>Requirement-based routing</h3>
          <p>Routes are planned around the pickup and delivery locations you share with us, rather than fixed lanes.</p>
        </div>
        <div class="service-card">
          <h3>Vehicle availability</h3>
          <p>Coverage for a given destination depends on suitable vehicle availability at the time of your request.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Check service availability for your route</h2>
          <p>Share your pickup and delivery locations and we will confirm what's possible.</p>
        </div>
        <div class="cta-band-actions">
          <a class="btn btn-primary" href="quote.html">Request a Quote</a>
          <a class="btn btn-outline-light" data-wa-link href="#">WhatsApp Us</a>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="Network & Service Areas | Mahashakthi Roadlines",
    description="Mahashakthi Roadlines operates from its head office in Madhavaram, Chennai, providing road transportation and logistics support across India.",
    active="network.html",
    body=body,
    canonical="network.html",
)
with open("/home/claude/mahashakthi/network.html", "w") as f:
    f.write(html)
print("network.html written", len(html))
