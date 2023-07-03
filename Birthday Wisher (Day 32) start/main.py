# import smtplib

# # sender = "Private Person <from@example.com>"
# sender = "Private Person <ronald@example.com>"

# # receiver = "A Test User <to@example.com>"
# receiver = "A Test User <brock@example.com>"


# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}

# This is a test e-mail message."""

# with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
#     server.login("325186a610ec82", "04d299f8725dd4")    
#     server.sendmail(sender, receiver, message)

# import datetime as dt

# now = dt.datetime.now()
# year = now.year # and so on

# print(now)

# dob = dt.datetime(1995, 12, 15)
# print(dob)
import datetime as dt
import smtplib
import random

sender = "barackobama@gmail.com"
receiver = "john@gmail.com"

# accessing today
now = dt.datetime.now()
today = now.strftime("%A")


# if today == "Monday":
    # accessing quotes.txt
with open(file="quotes.txt") as quotes:
    messages = quotes.readlines()
    quote = random.choice(messages)

# message = f"""\
# From: {sender}
# To: {receiver}
# Subject: Monday Motivation\n\n
# {quote}"""
message = f"""\
Subject: Monday Motivation\n\n
{quote}"""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.starttls()
    server.login("325186a610ec82", "04d299f8725dd4")
    server.sendmail(from_addr=sender, to_addrs=sender, msg=message)
    print("Complete")

