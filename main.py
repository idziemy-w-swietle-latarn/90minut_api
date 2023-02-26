import requests
from bs4 import BeautifulSoup



r = requests.post('http://www.90minut.pl/szukaj.php', {'tekst':'Cristian Omar', 'submit': 'SZUKAJ'}).text

soup = BeautifulSoup(r, 'html.parser')


print(soup.find(lambda tag:tag.name=='b' and "ZAWODNICY" in tag.text).parent)

soup = soup.find('td', {'class': 'main', 'width': '628', 'valign': 'top', 'bgcolor': '#FFFFFF', 'align': 'center'})
results = soup.find_all('td')[1::2]
print(results)