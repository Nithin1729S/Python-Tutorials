from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
yc_webpage=response.text

soup=BeautifulSoup(yc_webpage,"html.parser")
print(soup)
print(soup.title)
player=soup.find(name='a',class_='text-hvr-underline text-bold cb-font-16')
print(player.string)

#Getting Link of the Element
print(player.get('href'))

#Finding the country of the player
player_country=soup.find(name='div',class_="cb-font-12 text-gray")
print(player_country.getText())
print(player_country.string)

#Finding the rating of the player
player_rating=soup.find(name='div',class_='cb-col cb-col-17 cb-rank-tbl pull-right')
print(player_rating.string)



