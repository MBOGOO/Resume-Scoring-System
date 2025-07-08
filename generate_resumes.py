import os
import pandas as pd
from fpdf import FPDF

# 1. Make sure the resumes directory exists
resumes_dir = "resumes"
os.makedirs(resumes_dir, exist_ok=True)

# 2. Dummy resume contents
resume_texts = [
    "Alice Smith\nSoftware Engineer\nSkills: Python, Machine Learning\nExperience: 3 years",
    "Bob Johnson\nData Analyst\nSkills: SQL, Excel\nExperience: 2 years",
    "Carol Lee\nFrontend Developer\nSkills: HTML, CSS, JavaScript\nExperience: 4 years",
    "Dan Brown\nIntern\nSkills: None\nExperience: None"
]

# 3. Write dummy PDFs
for i, text in enumerate(resume_texts, start=1):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, text)
    resume_path = f"{resumes_dir}/resume{i}.pdf"
    pdf.output(resume_path)

# 4. Balanced labels (2 good resumes, 2 bad resumes)
# Let's say resume1, resume2 are GOOD (1), resume3, resume4 are BAD (0)
labels = [1, 1, 0, 0]

# 5. Save CSV file
df = pd.DataFrame(
    {"resume_path": [f"{resumes_dir}/resume{i}.pdf" for i in range(1, 5)], "score": labels}
)
df.to_csv("resumes.csv", index=False)

print("✅ Dummy PDFs and resumes.csv created!")
