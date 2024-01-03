import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.python.org/").text
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())

for link in soup.find_all('a', href=True):
    print(link['href'])
