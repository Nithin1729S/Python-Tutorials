import requests
from datetime import datetime

from smtplib import *
import time

my_email="johannliebert296@gmail.com"
my_password="aswyxvjjjizmxbnu"


time_now=datetime.now().hour

MY_LAT=12.994640
MY_LNG=74.798271


#Collecting ISS Data
def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_iss=response.json()

    iss_lat=data_iss['iss_position']["latitude"]
    iss_lng=data_iss['iss_position']["longitude"]

    #Your position is within +5 or -5 degrees of the iss position

    if MY_LAT-5<=iss_lat<=MY_LAT+5 and MY_LNG-5<=MY_LNG<=MY_LNG+5:
        return True

def is_it_night():
    parameters={"lat":MY_LAT,
                "lng":MY_LNG,
                "formatted":0}

    response=requests.get(url=" https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()


    sunrise=int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(':')[0])

    if time_now>=sunset or time_now<=sunrise:
        return True



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if is_it_night() and is_iss_overhead():
        with SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="nithins.221me139@nitk.edu.in",
                                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky.")





