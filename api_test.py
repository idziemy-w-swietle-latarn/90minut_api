import requests
from bs4 import BeautifulSoup



r = requests.post('http://www.90minut.pl/szukaj.php', {'tekst':'Cristian Diaz', 'submit': 'SZUKAJ'}).text

soup = BeautifulSoup(r, 'html.parser')


print(soup.find(lambda tag:tag.name=='b' and "ZAWODNICY" in tag.text).parent)