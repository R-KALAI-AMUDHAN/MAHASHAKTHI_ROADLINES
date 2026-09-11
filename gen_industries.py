import sys
sys.path.insert(0, "/home/claude/mahashakthi")
from build import page

industries = [
    ("Manufacturing", "Movement of raw materials, components and finished goods between manufacturing sites and distribution points."),
    ("Automotive", "Transportation support for automotive parts and related cargo requirements."),
    ("Construction", "Road transportation for construction materials and industrial supplies."),
    ("FMCG", "Regular movement of fast-moving consumer goods between depots and markets."),
    ("Retail & Distribution", "Transportation between warehouses, distributors and retail points."),
    ("Industrial Goods", "Cargo movement for industrial equipment and supplies, arranged per consignment."),
    ("Agriculture", "Road transportation support for agricultural goods and produce."),
    ("General Cargo", "Flexible transportation for cargo that doesn't fall into a specific category."),
    ("E-Commerce & Distribution", "Transportation support for e-commerce and distribution-related cargo movement."),
]

cells = "\n        ".join(
    '<div class="industry-cell reveal"><h3>{0}</h3><p>{1}</p></div>'.format(name, desc)
    for name, desc in industries
)

body = '''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb"><a href="index.html">Home</a> / Industries</div>
      <span class="eyebrow">Industries we serve</span>
      <h1>Sectors we can support</h1>
      <p>General cargo and sector-specific transportation requirements, arranged as they come in. These are sectors we can support, not a list of confirmed clients.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="industry-grid">
        ''' + cells + '''
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="grid grid-2 reveal" style="align-items:center;gap:40px;">
        <div>
          <h2>Don't see your industry listed?</h2>
          <p>These categories reflect the type of cargo we can generally support. If your requirement falls outside them, share the details and we will let you know what's possible.</p>
        </div>
        <div>
          <a class="btn btn-primary" href="quote.html">Request a Quote</a>
        </div>
      </div>
    </div>
  </section>
'''

html = page(
    title="Industries We Serve | Mahashakthi Roadlines",
    description="Mahashakthi Roadlines supports transportation requirements across manufacturing, automotive, FMCG, retail, construction, agriculture and general cargo.",
    active="industries.html",
    body=body,
    canonical="industries.html",
)
with open("/home/claude/mahashakthi/industries.html", "w") as f:
    f.write(html)
print("industries.html written", len(html))
