import smtplib
my_email="johannliebert296@gmail.com"
my_password="aswyxvjjjizmxbnu"
connection=smtplib.SMTP_SSL("smtp.gmail.com",port=587,timeout=120)
connection.starttls()
connection.login(user=my_email,password=my_password)
connection.sendmail(from_addr=my_email,to_addrs="bharatmajime@gmail.com",msg="Subject:Hello \n\n This is the body of my email")
connection.close()


