from fpdf import FPDF
import os
import random
import pandas as pd

# Ensure resumes directory exists
os.makedirs('resumes', exist_ok=True)

CAREER_FIELDS = [
    "Software Engineer", "Data Scientist", "Web Developer", "Network Engineer", "Cybersecurity Analyst",
    "Database Administrator", "AI Researcher", "Machine Learning Engineer", "Business Analyst", "Project Manager",
    "System Administrator", "Mobile App Developer", "IT Consultant", "UI-UX Designer", "DevOps Engineer",
    "Technical Writer", "Graphic Designer", "Cloud Architect", "Penetration Tester", "Financial Analyst",
    "Accountant", "Human Resource Manager", "Digital Marketer", "SEO Specialist", "Sales Representative",
    "Product Manager", "Electrical Engineer", "Mechanical Engineer", "Civil Engineer", "Architect",
    "Interior Designer", "Operations Manager", "Legal Advisor", "Quality Assurance Engineer", "Biomedical Engineer",
    "Content Writer", "Social Media Manager", "Network Architect", "Full Stack Developer", "Data Engineer",
    "IT Support Specialist", "Security Specialist", "Robotics Engineer", "Blockchain Developer", "Game Developer",
    "E-commerce Specialist", "Logistics Coordinator", "Agricultural Analyst", "Environmental Consultant", "Education Consultant"
]

data = []

def create_pdf(filepath, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(filepath)

# Generate minimum 5 resumes per career field
for career in CAREER_FIELDS:
    for _ in range(5):
        safe_career = career.replace(" ", "_").replace("/", "-")
        filename = f'resumes/{safe_career}_{random.randint(1000,9999)}.pdf'
        content = f"This is a resume for a {career}. Key skills include {career.lower()} work, collaboration, leadership."
        create_pdf(filename, content)
        data.append({'resume_path': filename, 'career_label': career})

# Generate 100 random extra resumes
for i in range(100):
    career = random.choice(CAREER_FIELDS)
    safe_career = career.replace(" ", "_").replace("/", "-")
    filename = f'resumes/random_{safe_career}_{random.randint(1000,9999)}.pdf'
    content = f"This is a resume for a {career}. Focus on skills like {career.lower()}, innovation, problem-solving."
    create_pdf(filename, content)
    data.append({'resume_path': filename, 'career_label': career})

# Save dataset
df = pd.DataFrame(data)
df.to_csv('resumes.csv', index=False)

print("✅ Valid PDF resumes and resumes.csv created successfully!")
