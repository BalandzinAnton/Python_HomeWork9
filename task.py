
import requests
from bs4 import BeautifulSoup as bs
url = 'https://www.mk.ru/anekdoti/'
response = requests.get(url).text
#print(response)
soup = bs(response, 'html.parser')
fun = soup.find('div', class_='listing-item__content').find('p', class_='listing-preview__desc').text
print(fun)

