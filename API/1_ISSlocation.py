import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# if response.status_code==400:
#     raise Exception("That Resource does not exist.")
# elif response.status_code==401:
#     raise Exception("You are note authorized to access this resource.")

response.raise_for_status()

data=response.json()
print(data)

longitude=data['iss_position']['longitude']
latitude=data["iss_position"]["latitude"]
print(longitude,longitude)


