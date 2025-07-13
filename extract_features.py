import os
from pdfminer.high_level import extract_text

# You can expand this list as needed
TECH_SKILLS = ['python', 'java', 'c++', 'excel', 'html', 'css', 'machine learning',
               'sql', 'javascript', 'react', 'node.js', 'php', 'laravel', 'c#']

def extract_features(resume_path):
    # Ensure the file exists
    if not os.path.exists(resume_path):
        return "", [0, 0, 0, 0]

    # Extract text from PDF
    try:
        text = extract_text(resume_path)
    except:
        text = ""

    text_lower = text.lower()

    # Basic numeric features
    num_words = len(text_lower.split())
    skill_count = sum(1 for skill in TECH_SKILLS if skill in text_lower)
    has_education = int('education' in text_lower)
    has_experience = int('experience' in text_lower)

    numeric_features = [num_words, skill_count, has_education, has_experience]

    return text, numeric_features
