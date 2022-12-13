import requests
from bs4 import BeautifulSoup
url = 'https://ycharts.com/indicators/bitcoin_average_difficulty'
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}

r = requests.get(url, headers=headers)

print(r)
print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
divs = soup.find('div', class_='key-stat-title')

print(divs.text)