import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

def fleet_card(icon, title, desc):
    return '''
        <div class="fleet-card reveal">
          <div class="art">{icon}</div>
          <div class="body"><h3>{title}</h3><p>{desc}</p></div>
        </div>'''.format(icon=icon, title=title, desc=desc)

ICON_LCV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="2" y="9" width="12" height="7" rx="1"/><path d="M14 11h4l3 2v3h-7z"/><circle cx="6" cy="17" r="1.7"/><circle cx="17" cy="17" r="1.7"/></svg>'
ICON_MGV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="1" y="8" width="14" height="8" rx="1"/><path d="M15 10h4l3 3v3h-7z"/><circle cx="6" cy="18" r="1.9"/><circle cx="18" cy="18" r="1.9"/></svg>'
ICON_HGV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="1" y="7" width="16" height="9" rx="1"/><path d="M17 9h4l2 4v3h-6z"/><circle cx="6" cy="18" r="1.9"/><circle cx="19" cy="18" r="1.9"/></svg>'
ICON_LARGE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="1" y="6" width="18" height="10" rx="1"/><path d="M19 8h3l1 4v3h-4z"/><circle cx="6" cy="18" r="1.9"/><circle cx="21" cy="18" r="1.9"/><line x1="7" y1="6" x2="7" y2="16"/><line x1="13" y1="6" x2="13" y2="16"/></svg>'
ICON_SPECIAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="2" y="9" width="13" height="7" rx="1"/><path d="M15 10h4l3 3v3h-7z"/><circle cx="6" cy="17" r="1.7"/><circle cx="17" cy="17" r="1.7"/><path d="M5 9V6h5v3"/></svg>'

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Our Fleet</div>
      <span class="eyebrow">Our fleet</span>
      <h1>A fleet arranged around your cargo</h1>
      <p>Mahashakthi Roadlines operates approximately 20 vehicles. Vehicle solutions can be arranged based on cargo type, volume, weight, route and customer requirements.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="notice reveal" style="margin-bottom:40px;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg>
        <span>We do not yet have professional photographs of our own vehicles. The illustrations below represent general vehicle categories, not specific trucks in our fleet. Photographs will be added here once available.</span>
      </div>
      <div class="grid grid-3">
''' + fleet_card(ICON_LCV, "Light Commercial Vehicles", "Suited to smaller consignments, shorter routes and time-sensitive local or regional movement.") \
    + fleet_card(ICON_MGV, "Medium Goods Vehicles", "A balance of capacity and manoeuvrability for medium-volume cargo across regional routes.") \
    + fleet_card(ICON_HGV, "Heavy Goods Vehicles", "Higher-capacity vehicles for bulkier consignments and longer-distance road transportation.") \
    + fleet_card(ICON_LARGE, "Large Capacity Vehicles", "For sizeable shipments requiring maximum available load capacity within our fleet.") \
    + fleet_card(ICON_SPECIAL, "Specialized Vehicle Options", "Vehicle options for specific cargo needs, discussed and arranged case by case.") + '''
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="grid grid-2 reveal" style="align-items:center;gap:40px;">
        <div>
          <h2>Availability depends on your requirement</h2>
          <p>Vehicle solutions can be arranged based on cargo type, volume, weight, route and customer requirements. Tell us what you need to move and we will match it to a suitable vehicle from our fleet.</p>
        </div>
        <div class="fleet-note">
          Approximately <strong>20 vehicles</strong> across multiple commercial vehicle types, arranged to fit the cargo requirement &mdash; capacity is confirmed at the time of booking based on your specific load.
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Tell us your requirement</h2>
          <p>Share your cargo details and we will confirm the right vehicle for the job.</p>
        </div>
        <div class="cta-band-actions">
          <a class="btn btn-primary" href="quote.html">Tell Us Your Requirement</a>
          <a class="btn btn-outline-light" href="tel:+919677079089">Call Us</a>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="Our Fleet | Mahashakthi Roadlines",
    description="Mahashakthi Roadlines operates approximately 20 vehicles across multiple commercial vehicle categories, arranged according to cargo type, volume and route.",
    active="fleet.html",
    body=body,
    canonical="fleet.html",
)
with open("/home/claude/mahashakthi/fleet.html", "w") as f:
    f.write(html)
print("fleet.html written", len(html))
