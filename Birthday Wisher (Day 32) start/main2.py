##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import os
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.strftime("%A")
today_date = now.date().strftime("%m-%d")
directory = "./letter_templates"
files = os.listdir(directory) # list of files
# print(files)
# print(today_date)

data = pd.read_csv("birthdays.csv")
data['birthday'] = pd.to_datetime(data[['year', 'month', 'day']])
data['date_without_year'] = data['birthday'].dt.strftime('%m-%d')

filtered_data = data[data['date_without_year'] == today_date]
print(filtered_data)
for index, row in filtered_data.iterrows():
    name = row['name']
    email = row['email']
    dob = row['birthday'].strftime('%Y-%m-%d')
    with open(f'{directory}/{random.choice(files)}') as file:
        letter = file.read()
        newLetter = letter.replace('[NAME]', name)
        # newLetter = [s.replace('[NAME]', name) for s in letter]
    
    sender = "ronaldrump@gmail.com"

    message = f"""\
    Subject: Happy Birthday!
    To: {email}
    From: {sender}
    {newLetter}
    """.encode('utf-8')

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login("325186a610ec82", "04d299f8725dd4")
        server.sendmail(sender, email, message)
        print("Sent")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




