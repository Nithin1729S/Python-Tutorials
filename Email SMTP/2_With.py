import smtplib

my_email="johannliebert296@gmail.com"
my_password="aswyxvjjjizmxbnu"
with smtplib.SMTP("smtp.gmail.com",port=587,timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="bharatmajime@gmail.com",
                        msg="Subject:Hello \n\n This is the body of my email")


#no connection.close() required