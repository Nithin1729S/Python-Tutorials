import pandas
from bs4 import BeautifulSoup
import requests
html_code=requests.get("https://myanimelist.net/topanime.php").text

soup=BeautifulSoup(html_code,'html.parser')

animes=[i.getText() for i in soup.find_all(name='h3',class_='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3')]

scores=[float(i.getText()) for i in soup.find_all(name="span",class_="text on score-label score-9")]+[float(i.getText()) for i in soup.find_all(name="span",class_="text on score-label score-8")]

data_dict={'animes':animes,'scores':scores}

data=pandas.DataFrame(data_dict).to_csv('top_mal_animes.csv')

