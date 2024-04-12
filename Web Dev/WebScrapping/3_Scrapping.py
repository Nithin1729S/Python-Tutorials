from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
yc_webpage=response.text

soup=BeautifulSoup(yc_webpage,"html.parser")


players=soup.find_all(name='a',class_="text-hvr-underline text-bold cb-font-16")
name = []
links=[]
for player in players:
    text=player.getText()
    name.append(text)

    link=player.get('href')
    links.append(link)

ratings=[int(score.getText()) for score in soup.find_all(name='div',class_='cb-col cb-col-17 cb-rank-tbl pull-right')]

country=[i.getText() for i in soup.find_all(name='div',class_="cb-font-12 text-gray")]
print(name)
print(links)
print(ratings)
print(country)







