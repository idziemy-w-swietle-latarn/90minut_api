import requests
from bs4 import BeautifulSoup
import json


r = requests.post('http://www.90minut.pl/szukaj.php', {'tekst':'Cristian Omar', 'submit': 'SZUKAJ'}).text

soup = BeautifulSoup(r, 'html.parser')

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

# print(soup.find(lambda tag:tag.name=='b' and "ZAWODNICY" in tag.text).parent)

# soup = soup.find('td', {'class': 'main', 'width': '628', 'valign': 'top', 'bgcolor': '#FFFFFF', 'align': 'center'})
# results = soup.find_all('td')[1::2]
# print(results)

test = {'dsds':'dsds', 'dsdsd':'dsdsds'}
test = AttrDict(test)
print(json.dumps(test))
print(test.dsds)