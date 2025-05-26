import pandas as pd

df = pd.read_excel('Data.xlsx')

df = df.drop_duplicates(subset='email')

df['has_joined_event'] = df['has_joined_event'].map({'Yes': True, 'No': False})

df['linkedin_missing'] = df['What is your LinkedIn profile?'].apply(
    lambda x: not isinstance(x, str) or not x.startswith('http'))

df['job_title_missing'] = df['Job Title'].isna() | (df['Job Title'].str.strip() == '')

df.to_csv("cleaned_output.csv", index=False)
