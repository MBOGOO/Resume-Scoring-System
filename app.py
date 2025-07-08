# app.py
from flask import Flask, request, render_template
import pickle
from extract_features import extract_features
import os

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score', methods=['POST'])
def score_resume():
    file = request.files['resume']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        features = extract_features(file_path)
        score = model.predict([features])[0]

        # Suggest simple feedback
        feedback = []
        if features[2] == 0:
            feedback.append('Add an education section.')
        if features[3] == 0:
            feedback.append('Add an experience section.')
        if features[1] < 2:
            feedback.append('Add more technical skills.')

        return render_template('result.html', score=score, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
