import re

file_path = r'c:\xampp\htdocs\CRC\who-we-are.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Replace Yousouf's section
yousouf_pattern = r'<div class="row align-items-start g-4">\s+<!-- Yousouf Image \+ Name -->.*?</p>\s+</div>'
yousouf_replacement = '''<!-- Yousouf Jhugroo - Professional Card -->
      <div class="card mb-5" style="border-radius: 20px; overflow: hidden; box-shadow: 0 10px 40px rgba(1, 33, 105, 0.15); border: none;">
        <div class="row g-0">
          <!-- Left Side - Gradient Background with Image -->
          <div class="col-lg-4" style="background: linear-gradient(135deg, #012169 0%, #003087 100%); padding: 3rem 2rem; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <img
              src="https://lirp.cdn-website.com/07d7be76/dms3rep/multi/opt/Yousouf_TmnkO8vQ1qiAiETyeGbw-300x300-1920w.jpg"
              class="img-fluid rounded-circle mb-3" width="180" alt="Yousouf Jhugroo" style="border: 5px solid white; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
            <h3 class="text-white fw-bold mb-2 text-center" style="font-family: 'Poppins', sans-serif;">Yousouf Jhugroo</h3>
            <div class="px-3 py-2 mb-2" style="background: rgba(255, 255, 255, 0.2); border-radius: 20px; backdrop-filter: blur(10px);">
              <span class="text-white fw-bold" style="font-size: 0.9rem;">Chairman & CEO</span>
            </div>
            <div class="text-center mt-3">
              <span class="badge me-2 mb-2" style="background: rgba(255, 255, 255, 0.25); color: white; font-size: 0.75rem;">LLM</span>
              <span class="badge me-2 mb-2" style="background: rgba(255, 255, 255, 0.25); color: white; font-size: 0.75rem;">MSc Health Services</span>
              <span class="badge me-2 mb-2" style="background: rgba(255, 255, 255, 0.25); color: white; font-size: 0.75rem;">ICA Fellow</span>
            </div>
          </div>
          
          <!-- Right Side - White Background with Content -->
          <div class="col-lg-8" style="padding: 3rem;">
            <div class="mb-3">
              <span class="badge" style="background: linear-gradient(90deg, #C8102E 0%, #A00E26 100%); color: white; padding: 0.5rem 1rem; font-size: 0.85rem; border-radius: 20px;">Founder & Chief Executive</span>
            </div>
            <h4 class="fw-bold mb-4" style="color: #012169; font-family: 'Poppins', sans-serif; font-size: 1.5rem;">CRC Chairman and CEO</h4>
            
            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
              Yousouf Jhugroo is the Founder of CRC and its five sub-divisional group of companies.
            </p>

            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
              Former CEO of the Institute for Consumer Protection (ICP) - a Consumers International Member organisation,
              Yousouf has over 20 years' experience in the world consumer movement. Yousouf has ran various training
              workshops on Consumer Education in Africa and has been a visiting Lecturer at the Mauritius Institute of
              Education (A Government Teachers' training institution, part of the University of Mauritius).
            </p>

            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
              As a Consumer Advocate, Yousouf has served on various Government Boards, such Central Water Authority,
              Central Electricity Board and the Mauritius Meat Authority.
            </p>

            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
              Yousouf is a certified Real Estate Manager from the Dubai Real Estate Institute, a division of Dubai Land
              Department.
            </p>

            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
              Fellow of the International Compliance Association (ICA), Yousouf has held senior compliance and contracts'
              management positions in the railway industry and was Head of Compliance for a national regulatory body in
              the UK energy efficiency sector. He has also been a senior associate of many NGOs such as the International
              Baby Foods Action Network (IBFAN). He also served as Baby Friendly Hospital Initiative Consultant for UNICEF
              and Governments Health Authorities in various countries of Africa.
            </p>

            <p style="color: #555; line-height: 1.8;">
              Yousouf has studied LLM with the University of Law and MSc in Health Services in UK.
            </p>
          </div>
        </div>
      </div>

      <div class="row align-items-start g-4">'''

content = re.sub(yousouf_pattern, yousouf_replacement, content, count=1, flags=re.DOTALL)

# Replace Paul's section (which is now already in card format - let's remove the duplicate rows)
paul_old = r'</div>\s+</div>\s+</section>\s+<section class="container my-5">'
paul_new = '''</div>
    </section>
    <section class="container my-5">'''

content = re.sub(paul_old, paul_new, content, count=1, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("✓ Yousouf and Paul profiles styled successfully!")
