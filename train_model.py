import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from extract_features import extract_features

# Load dataset
df = pd.read_csv('resumes.csv')

texts = []
labels = []

print("🔍 Extracting text from resumes...")

for index, row in df.iterrows():
    text, numeric_feats = extract_features(row['resume_path'])
    texts.append(text)            # Use extracted text
    labels.append(row['career_label'])  # Use career field

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(texts)
y = labels

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train Logistic Regression Model
print("🚀 Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained successfully! Test Accuracy: {accuracy * 100:.2f}%")

# Save Model and Vectorizer
joblib.dump(model, 'career_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
print("💾 Model and vectorizer saved.")
