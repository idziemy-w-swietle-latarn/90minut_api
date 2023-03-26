import requests
from bs4 import BeautifulSoup

BASE_LINK = 'http://www.90minut.pl'
KARIERA = '/kariera.php?id='
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
}

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_page_soup(link):
    html_text = requests.get(link, headers=headers).text
    return BeautifulSoup(html_text, 'html.parser')

def get_player_season(player_id, season_id):
    link = 'http://www.90minut.pl/wystepy.php?id={}&id_sezon={}'.format(player_id, season_id)
    soup = get_page_soup(link)
    player_dict = AttrDict()
    player_dict.link = link
    player_dict.season = soup.find("div", {'id': '90minut_kariera_zawodnika_belka'}).next_sibling.next_sibling
    player_dict.season = player_dict.season.p.b.text.split()[-1].strip()
    tables = soup.find_all('table', {'class':"main", 'width':'800', 'border':'0'})
    player_dict.games = tables[1].find_all('tr', recursive=False)[1:]
    for n, game in enumerate(player_dict.games):
        base = game
        game = AttrDict()
        game.date = base.td.nobr.text.split()[0].strip()
        game.hour = base.td.nobr.text.split()[1].strip()
        game.competition = base.td.next_sibling.text
        
        player_dict.games[n] = game

    return player_dict
    
def search(search_phrase, search_mode = 'szukaj'):
    html_text = requests.post('http://www.90minut.pl/szukaj.php', 
                              {'tekst': search_phrase, 'submit': search_mode}, headers=headers).text
    soup = BeautifulSoup(html_text, 'html.parser')
    soup = soup.find('td', {'class': 'main', 'width': '628', 
                            'valign': 'top', 'bgcolor':'#FFFFFF', 'align':'center'})
    soup = soup.find_all('div')
    results_dict = {}
    for div in soup:
        key = div.b.text.strip()
        results_dict[key] = {}
        div = div.next_sibling.next_sibling.find_all('tr')
        if key == 'ZAWODNICY':
            for tr in div:
                base = tr.find_all('td')[1]
                player_name = base.text.strip()
                player_link = base.a['href']
                results_dict[key][player_name] = player_link
        elif key == 'KLUBY':
            pass
        elif key == 'SĘDZIOWIE':
            pass
        
    return results_dict
    
    
def get_first_finding(search_phrase):
    # link = search(search_phrase)[0].link
    # soup = get_page_soup(link)
    pass
    
def parse_player(id):
    link = BASE_LINK + KARIERA + id
    soup = get_page_soup(link)
    player_dict = AttrDict()
    player_dict.link = KARIERA + id
    player_dict.name = soup.find('td', string="Imię").next_sibling.text
    player_dict.surname = soup.find('td', string="Nazwisko").next_sibling.text
    player_dict.birthplace = soup.find('td', string="Miejsce urodzenia").next_sibling.text
    player_dict.position = soup.find('td', string="Pozycja").next_sibling.text
    matches_goals = soup.find('td', string='liga polska').parent.find_all('td')
    player_dict.goals = matches_goals[-2].text
    player_dict.games = matches_goals[-3].text
    player_dict.birthdate = soup.find('td', string="Data urodzenia").next_sibling.text[0:-8].strip()
    player_dict.height = soup.find('td', string="Wzrost / waga").next_sibling.text.split('/')[0].strip()
    seasons = soup.find('div', {'id': '90minut_kariera_zawodnika_belka'})
    seasons = seasons.parent.table.find_all('tr')[1:-1]
    player_dict.seasons = []
    for season in seasons:
        season_dict = AttrDict()
        season = season.find_all('td')
        season_dict.season = season[0].text
        if season[0].a:
            season_dict.link = season[0].a.get('href')
        else:
            season_dict.link = ''
        if season[1].text == '-':
            season_dict.country = ''
            season_dict.club = ''
            season_dict.link_club = ''
        else:
            season_dict.club = season[1].a.text
            season_dict.country = season[1].img['title']
            season_dict.link_club = season[1].a['href']
        season_dict.matches = season[2].text
        season_dict.goals = season[3].text
        season_dict.trophies = season[4].text.split('\n')
        
        player_dict.seasons.append(season_dict)
        
    return player_dict