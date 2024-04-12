import pandas
from bs4 import BeautifulSoup
import requests
html_code=requests.get("https://myanimelist.net/topmanga.php?type=manga").text

soup=BeautifulSoup(html_code,'html.parser')

mangas=[i.getText() for i in soup.find_all(name='a',class_="hoverinfo_trigger fs14 fw-b")]
scores=[i.getText() for i in soup.find_all(name='span',class_="text on score-label score-9")]+[i.getText() for i in soup.find_all(name='span',class_="text on score-label score-8")]

data_dict={'animes':mangas,'scores':scores}

data=pandas.DataFrame(data_dict).to_csv('top_mal_mangas.csv')
