import re

file_path = r'c:\xampp\htdocs\CRC\who-we-are.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print("Starting comprehensive profile updates...")

# Function to create a modern card profile
def create_card_profile(name, role, badge, image_url, paragraphs, skills):
    para_html = ""
    for i, p in enumerate(paragraphs):
        if i < len(paragraphs) - 1:
            para_html += f'''            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
              {p}
            </p>

'''
        else:
            para_html += f'''            <p style="color: #555; line-height: 1.8;">
              {p}
            </p>'''
    
    skills_html = ''.join([f'              <span class="badge me-2 mb-2" style="background: rgba(255, 255, 255, 0.25); color: white; font-size: 0.75rem;">{skill}</span>\n' for skill in skills])
    
    return f'''      <!-- {name} - Professional Card -->
      <div class="card mb-5" style="border-radius: 20px; overflow: hidden; box-shadow: 0 10px 40px rgba(200, 16, 46, 0.15); border: none;">
        <div class="row g-0">
          <!-- Right Side - White Background with Content -->
          <div class="col-lg-8 order-lg-1 order-2" style="padding: 3rem;">
            <div class="mb-3">
              <span class="badge" style="background: linear-gradient(90deg, #012169 0%, #003087 100%); color: white; padding: 0.5rem 1rem; font-size: 0.85rem; border-radius: 20px;">{badge}</span>
            </div>
            <h4 class="fw-bold mb-4" style="color: #C8102E; font-family: 'Poppins', sans-serif; font-size: 1.5rem;">{role}</h4>
            
{para_html}
          </div>
          
          <!-- Left Side - Gradient Background with Image -->
          <div class="col-lg-4 order-lg-2 order-1" style="background: linear-gradient(135deg, #C8102E 0%, #A00E26 100%); padding: 3rem 2rem; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <img
              src="{image_url}"
              class="img-fluid rounded-circle mb-3" width="180" alt="{name}" style="border: 5px solid white; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
            <h3 class="text-white fw-bold mb-2 text-center" style="font-family: 'Poppins', sans-serif;">{name}</h3>
            <div class="px-3 py-2 mb-2" style="background: rgba(255, 255, 255, 0.2); border-radius: 20px; backdrop-filter: blur(10px);">
              <span class="text-white fw-bold" style="font-size: 0.9rem;">{role[:30]}</span>
            </div>
            <div class="text-center mt-3">
{skills_html}            </div>
          </div>
        </div>
      </div>'''

# Update Dr. Heba Shahein
dr_heba_old = r'<!-- Column 1: Image \+ Name -->\s+<div class="col-12 col-md-2 text-center">\s+<img src="https://lirp\.cdn-website\.com/07d7be76/dms3rep/multi/opt/unnamed\+2-1920w\.jpg".*?</div>\s+<!-- Column 2: Director Title.*?Based in London, Dr Shahein is Egyptian and she speaks fluently English, French and Arabic\.\s+</p>\s+</div>'

dr_heba_new = create_card_profile(
    "Dr. Heba Shahein",
    "Non-Executive Director (Overseeing CRC Middle East)",
    "Board Director",
    "https://lirp.cdn-website.com/07d7be76/dms3rep/multi/opt/unnamed+2-1920w.jpg",
    [
        "Holder of a PhD in Law from London School of Economics (LSE), Dr Heba Shahein has 25 years of experience in research, strategic planning and leadership and practicing law. She has been a visiting Lecturer in EU Competition Law and English Contract law at King's College London (KCL) since 2012 where she also studied for her postgraduate diploma. Dr Shahein has a Master's in law (LLM) from Amsterdam University.",
        "Dr Shahein was also Vice Chairperson of the Egyptian Competition Authority (ECA) from 2007-2011.",
        "In addition to her academic achievements, Dr Shahein provided consultancy services to the World Bank on reforming laws. She was involved in various projects for government and regulatory bodies in Brazil, Colombia, Egypt, Kuwait, Oman, Thailand and the UK.",
        "Dr Shahein has provided training to project leaders and executives of the National Broadcasting and Telecommunications Commission in Thailand; she was also provided technical assistance for the reform of laws to the Public Authority for Consumer Protection (PACP) in London and Oman. In 2015, Dr Shahein provided legal services and technical legal advice on reform of merger control rules to the Egyptian Competition Authority.",
        "Dr Shahein is a specialist in corporate, commercial, EU and competition laws.",
        "Based in London, Dr Shahein is Egyptian and she speaks fluently English, French and Arabic."
    ],
    ["PhD Law (LSE)", "LLM", "Competition Law", "World Bank Consultant"]
)

content = re.sub(dr_heba_old, dr_heba_new, content, flags=re.DOTALL)

# Update Jonathan Harley
jonathan_old = r'<!-- Column 3: Image \+ Name -->\s+<div class="col-12 col-md-2 text-center">\s+<img\s+src="https://lirp\.cdn-website\.com/07d7be76/dms3rep/multi/opt/ce050cb8-844d-45a1-aa0e-485c34b54e83-1920w\.jpg".*?Clients include.*?large multi-nationals\.\s+</p>\s+</div>'

jonathan_new = create_card_profile(
    "Jonathan Harley",
    "Senior Consultant",
    "Board Consultant",
    "https://lirp.cdn-website.com/07d7be76/dms3rep/multi/opt/ce050cb8-844d-45a1-aa0e-485c34b54e83-1920w.jpg",
    [
        "Jonathan has extensive experience in the Utilities sector and is currently on the Leadership Team at a London city-based Consultancy and Advisory firm. As well as a background in Operations, Policy and Regulation, Jonathan has managed a number of Government policy implementation programmes.",
        "Jonathan has both UK and international experience having worked in Taipei, Tokyo, Brussels and Delhi. Clients include the Department of Energy and Climate Change (DECC), Office of Communications (OFCOM), Office of Gas and Electricity Markets (OFGEM) and the Japanese Ministry for Environment as well as a number of large multi-nationals."
    ],
    ["Utilities Expert", "Policy & Regulation", "International Experience"]
)

content = re.sub(jonathan_old, jonathan_new, content, flags=re.DOTALL)

# Save the updated content
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("✓ Dr. Heba Shahein profile updated!")
print("✓ Jonathan Harley profile updated!")
print("✓ Continuing with remaining profiles...")
print("\nNext: Programme Managers (Sonny, Dr. Eric, Mehwish)")
