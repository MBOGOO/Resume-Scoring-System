import pandas as pd

df = pd.read_csv('resumes.csv')
print("\n=== Raw data ===")
print(df)

print("\n=== Count of each score ===")
print(df['score'].value_counts())  # Check label distribution
