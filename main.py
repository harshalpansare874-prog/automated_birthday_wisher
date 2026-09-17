import datetime
import pandas as pd
import os
from dotenv import load_dotenv
import random
import smtplib

load_dotenv()

data = pd.read_csv("birthdays.csv")
today = datetime.datetime.now()

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
folder = "letter_templates"
files = os.listdir(folder)

for index, row in data.iterrows():
    if row["month"] == today.month and row["day"] == today.day:

        random_file = random.choice(files)

        with open(os.path.join(folder, random_file), "r") as f:
            content = f.read()

            content = content.replace("[NAME]", row["name"])
            content = content.replace("Angela", "Harshal")
            RECEIVER = row["email"]

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs= RECEIVER,
                                msg = f"Subject: Birthday Wishes\n\n{content}")
