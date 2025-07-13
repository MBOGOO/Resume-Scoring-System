import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import joblib
from extract_features import extract_features  # Ensure your extract_features returns text + numeric features

app = Flask(__name__)

# Load your trained model and vectorizer
model = joblib.load('career_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['resume']
    filename = secure_filename(file.filename)
    os.makedirs('temp', exist_ok=True)
    file_path = os.path.join('temp', filename)
    file.save(file_path)

    text, numeric_features = extract_features(file_path)
    text_features = vectorizer.transform([text])

    probabilities = model.predict_proba(text_features)[0]
    top_indices = probabilities.argsort()[::-1][:5]

    results = [
        {"career": model.classes_[index], "confidence": round(probabilities[index] * 100, 2)}
        for index in top_indices
    ]

    # Calculate Resume Quality Score
    skill_count = numeric_features[1]
    num_words = numeric_features[0]
    max_confidence = max(probabilities)

    quality_score = min(100, 
        (skill_count / 10) * 50 + 
        (num_words / 500) * 30 + 
        max_confidence * 20 * 5
    )
    quality_score = round(quality_score, 2)

    return render_template('result.html', results=results, quality_score=quality_score)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
