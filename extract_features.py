# extract_features.py
import re
from pdfminer.high_level import extract_text

TECH_SKILLS = ['python', 'java', 'c++', 'excel', 'html', 'css', 'machine learning']

def extract_features(resume_path):
    text = extract_text(resume_path).lower()
    num_words = len(text.split())
    skill_count = sum(1 for skill in TECH_SKILLS if skill in text)
    has_education = int('education' in text)
    has_experience = int('experience' in text)
    return [num_words, skill_count, has_education, has_experience]
