import requests
from bs4 import BeautifulSoup

BASE_LINK = 'http://www.90minut.pl'
KARIERA = '/kariera.php?id='

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def get_page_soup(link):
    html_text = requests.get(link).text
    return BeautifulSoup(html_text, 'html.parser')

def search_results(search_phrase):
    pass

def get_first_finding(search_phrase):
    link = search_results(search_phrase)[0].link
    soup = get_page_soup(link)
    
def parse_player(id):
    link = BASE_LINK + KARIERA + id
    soup = get_page_soup(link)
    player_dict = AttrDict()
    player_dict.link = KARIERA + id
    player_dict.name = soup.find('td', string="Imię").next_sibling.text
    player_dict.surname = soup.find('td', string="Nazwisko").next_sibling.text
    player_dict.birthplace = soup.find('td', string="Miejsce urodzenia").next_sibling.text
    player_dict.position = soup.find('td', string="Pozycja").next_sibling.text

    return player_dict