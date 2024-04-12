from bs4 import BeautifulSoup
import lxml

with open ("website.html",encoding='utf8') as file:
    contents=file.read()

soup=BeautifulSoup(contents,'html.parser')
print(soup.title)
print(soup.prettify())
print(soup.title.string)

all_anchor_tags=soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.getText())

for tag in all_anchor_tags:
    print(tag.get('href'))

particular_heading=soup.find_all(name='h1',id='name')
print(particular_heading)


section_heading=soup.find(name='h3',class_='heading')
print(section_heading.getText())
print(section_heading.get('class'))

company_url=soup.select_one(selector='p a')
print(company_url)

name=soup.select_one(selector='#name')
print(name)

headings=soup.select('.heading')
print(headings)





