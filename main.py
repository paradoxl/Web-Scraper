import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.washingtonpost.com/books/2022/12/08/best-mystery-novels-2022/')

print(r)
print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
divs = soup.find('article', class_='grid-article mb-xxl-ns')
lines = divs.find_all('p')
for div in divs:
    for line in lines:
        print(line.text)