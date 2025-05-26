import pandas as pd
import json
import os

def generate_message(row):
    name = row['first_name'] if pd.notna(row['first_name']) else row['name'].split()[0]
    job_title = row['Job Title'] if pd.notna(row['Job Title']) else "professional"
    has_linkedin = pd.notna(row['What is your LinkedIn profile?']) and row['What is your LinkedIn profile?'].lower() not in ['none', 'nil', 'no', 'n/a', '']
    
    if row['has_joined_event'] == 'Yes':
        message = f"Hey {name}, thanks for joining our session! As a {job_title.lower()}, we think you'll love our upcoming AI workflow tools."
        if has_linkedin:
            message += " Let's connect on LinkedIn to keep you updated!"
        else:
            message += " Want early access?"
    else:
        message = f"Hi {name}, sorry we missed you at the last event! We're preparing another session that might better suit your interests as a {job_title.lower()}."
        if has_linkedin:
            message += " I'd love to connect and learn more about what topics interest you."
        else:
            message += " Would you like us to notify you about future events?"
    
    return message

def main():
    df = pd.read_excel(r'D:\VS Code\Intern Project\Data.xlsx')

    df['message'] = df.apply(generate_message, axis=1)
    os.makedirs('user_messages', exist_ok=True)
    df[['email', 'message']].to_csv('custom_messages.csv', index=False)
    
    for _, row in df.iterrows():
        user_data = {
            'name': row['name'],
            'email': row['email'],
            'job_title': row['Job Title'],
            'joined_event': row['has_joined_event'],
            'has_linkedin': pd.notna(row['What is your LinkedIn profile?']) and row['What is your LinkedIn profile?'].lower() not in ['none', 'nil', 'no', 'n/a', ''],
            'message': row['message']
        }
        filename = f"user_messages/{row['name'].replace(' ', '_').lower()}_message.json"
        with open(filename, 'w') as f:
            json.dump(user_data, f, indent=2)

    print("Messages generated successfully! Check custom_messages.csv and the user_messages folder.")

if __name__ == "__main__":
    main()
