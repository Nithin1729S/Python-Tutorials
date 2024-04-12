import pandas
from bs4 import BeautifulSoup
import requests
html_code=requests.get("https://www.imdb.com/chart/top/").text

soup=BeautifulSoup(html_code,'html.parser')

movies=[i.getText().replace(" ","").replace("\n","").split(".")[1] for i in soup.find_all(name="td",class_='titleColumn')]


movies_=[i.getText().replace(" ","").replace("\n","") for i in soup.find_all(name="td",class_='titleColumn')]

ratings=[float(i.getText().strip()) for i in soup.find_all(name="td",class_='ratingColumn imdbRating')]



with open("topmovies.txt",mode='w') as file:
    for i in movies_:
        file.write(f"{i}\n")


data_dict={"Movie":movies,"Rating":ratings}

data=pandas.DataFrame(data_dict).to_csv("top_IMDB_movies_ALL_TIME.csv")

