import pandas
from bs4 import BeautifulSoup
import requests
html_code=requests.get("https://myanimelist.net/character.php").text

soup=BeautifulSoup(html_code,'html.parser')

characters=[i.getText() for i in soup.find_all(name='a',class_='fs14 fw-b')]
favourites=[(i.getText().strip().replace(",",""))for i in soup.find_all(name='td',class_='favorites') if i!='favorites']
favourites.pop(0)
favourites=[int(i) for i in favourites]



zipped=dict(zip(characters,favourites))

data_dict={'names':characters,'favourites':favourites}
print(data_dict)

data=pandas.DataFrame(data_dict)
print(data)

data.to_csv('anime_characters_favourites.csv')


