Intern Project: Event Data Automation
Overview
This project has Python scripts to clean event data, create personalized messages, and send emails automatically.

Files
data.xlsx — original dataset

clean_data.py — cleans data (removes duplicates, normalizes columns, flags missing info) and outputs cleaned_output.csv

cleaned_output.csv — cleaned data file

generated_messages.py — creates personalized messages based on data and saves custom_messages.csv and individual user JSON files

custom_messages.csv — emails and messages to send

send_email.py — sends emails using SMTP with the messages from custom_messages.csv

How to Run:

Run clean_data.py to clean the data

Run generated_messages.py to create messages

Run send_email.py to send emails

Make sure you have Python installed and the pandas package (pip install pandas).
Update send_email.py with your email and app password before running.

Author
Rahul Verma
LinkedIn:https://www.linkedin.com/in/rahul-verma-a5b879256/