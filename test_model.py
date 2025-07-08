import pickle
from extract_features import extract_features

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Test a resume
sample_path = 'resumes/resume1.pdf'
features = extract_features(sample_path)
prediction = model.predict([features])[0]

print(f"Predicted score: {prediction}")

