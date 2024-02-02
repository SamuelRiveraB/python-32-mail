import smtplib
import datetime as dt
import random

import pandas

my_email = "t0675334@gmail.com"
password = "sglnxemwtmdbzbom"

now = dt.datetime.now()
day = now.day
month = now.month

bdays = pandas.read_csv("birthdays.csv")
bdays = bdays.to_dict(orient="records")

for bd in bdays:
    if bd["day"] == day and bd["month"] == month:
        bd_name = bd["name"]
        with open('letter.txt') as lt:
            lett = lt.readlines()
            lett[0] = lett[0].replace("[name]", bd_name)
            mail_body = "".join(lett)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Happy Birthday\n\n{mail_body}")
