import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from extract_features import extract_features

df = pd.read_csv('resumes.csv')
X = [extract_features(path) for path in df['resume_path']]
y = df['score']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42, stratify=y
)
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print('Model trained successfully!')
