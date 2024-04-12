from smtplib import *
from datetime import *
import random

my_email="johannliebert296@gmail.com"
my_password="aswyxvjjjizmxbnu"


now=datetime.now()
day_of_the_week=now.weekday()
print(day_of_the_week)
if day_of_the_week==5:
    with open("quotes.txt") as quotes:
        all_quotes=quotes.readlines()
        quote=random.choice(all_quotes)

    print(quote)

    with SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="nithins.221me139@nitk.edu.in",msg=f"Subject:Monday Motivation\n\n{quote}")










