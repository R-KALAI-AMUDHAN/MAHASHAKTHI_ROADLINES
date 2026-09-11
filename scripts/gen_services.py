import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

def svc(icon, title, desc, benefits):
    items = "\n            ".join('<li>{0}</li>'.format(b) for b in benefits)
    return '''
      <div class="grid grid-2 reveal" style="align-items:center;gap:40px;padding:44px 0;border-bottom:1px solid var(--gray-200);">
        <div>
          <div class="fleet-card" style="border:none;">
            <div class="art" style="border-radius:6px;">{icon}</div>
          </div>
        </div>
        <div>
          <h2 style="font-size:1.5rem;">{title}</h2>
          <p>{desc}</p>
          <ul>
            {items}
          </ul>
          <a class="btn btn-primary" href="quote.html">Request Transportation</a>
        </div>
      </div>
'''.format(icon=icon, title=title, desc=desc, items=items)

ICON_TRUCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" width="140" height="140"><rect x="1" y="7" width="14" height="10" rx="1"/><path d="M15 10h4l3 3v4h-7z"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="19" r="2"/></svg>'
ICON_FREIGHT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" width="140" height="140"><path d="M4 17h2l1-5h10l1 5h2"/><path d="M7 12 9 6h6l2 6"/><circle cx="8" cy="19" r="1.6"/><circle cx="16" cy="19" r="1.6"/></svg>'
ICON_WAREHOUSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" width="140" height="140"><path d="M3 9.5 12 4l9 5.5V19a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M8 20v-7h8v7"/></svg>'
ICON_LOGISTICS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" width="140" height="140"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/></svg>'
ICON_DEDICATED = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" width="140" height="140"><rect x="2" y="8" width="20" height="9" rx="1"/><path d="M2 12h20M8 8v9M16 8v9"/></svg>'
ICON_CUSTOM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" width="140" height="140"><path d="M4 4h16v6H4zM4 14h10v6H4zM17 14h3v6h-3z"/></svg>'

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Services</div>
      <span class="eyebrow">Services</span>
      <h1>Road transportation &amp; logistics services</h1>
      <p>Vehicle solutions and logistics support arranged around your cargo, route and delivery timeline.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
''' + svc(ICON_TRUCK, "Goods Transportation", "Reliable road transportation for different types of cargo, from single consignments to recurring shipments.", [
    "Vehicles arranged to suit the cargo type and volume",
    "Coverage across destinations in India",
    "Direct coordination on pickup and delivery timing",
]) + svc(ICON_FREIGHT, "Road Freight", "Efficient road-based movement of goods across destinations in India, using vehicles suited to the load and route.", [
    "Roadways-only operation across India",
    "Vehicle type matched to route and cargo",
    "Coordination for multi-stop or single-destination freight",
]) + svc(ICON_WAREHOUSE, "Warehousing", "Storage and handling solutions to support supply-chain requirements alongside transportation.", [
    "Handling support tied to transportation schedules",
    "Arrangements discussed based on volume and duration",
    "Coordinated pickup from storage to onward transport",
]) + svc(ICON_LOGISTICS, "Logistics Support", "Transportation and logistics support tailored to business requirements, from planning to delivery.", [
    "Requirement-based planning for cargo movement",
    "Support for recurring or one-time transportation needs",
    "Coordination across pickup, transit and delivery",
]) + svc(ICON_DEDICATED, "Dedicated Vehicle Solutions", "Vehicle arrangements based on cargo requirements, giving a dedicated vehicle for your consignment.", [
    "A vehicle assigned specifically to your shipment",
    "Suited to time-sensitive or sizeable consignments",
    "Capacity arranged according to your requirement",
]) + svc(ICON_CUSTOM, "Customized Transportation", "Flexible transportation arrangements depending on cargo type, quantity and destination.", [
    "Arrangements built around your specific cargo",
    "Flexibility on quantity, packaging and destination",
    "Discussed directly to fit your operational needs",
]) + '''
    </div>
  </section>

  <section class="section section--navy">
    <div class="container">
      <div class="cta-band reveal" style="background:var(--navy-800);">
        <div>
          <h2>Not sure which service fits your requirement?</h2>
          <p>Share your cargo and route details and we will arrange a suitable transportation solution.</p>
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
    title="Services | Mahashakthi Roadlines",
    description="Goods transportation, road freight, warehousing, logistics support, dedicated vehicles and customized transportation from Mahashakthi Roadlines, Chennai.",
    active="services.html",
    body=body,
    canonical="services.html",
)
with open("/home/claude/mahashakthi/services.html", "w") as f:
    f.write(html)
print("services.html written", len(html))
