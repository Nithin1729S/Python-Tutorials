from json import load,loads,dump,dumps
import requests
response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)


with open("issData.json") as file:
    pythonDict=load(file)

jsonData=response.json()
jsonStringData=dumps(jsonData)

with open("issDumps.json","w") as file:
    print("Now writing ISS Data.....")
    print()
    file.write(jsonStringData)


