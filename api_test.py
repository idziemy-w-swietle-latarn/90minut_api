from api import get_first_finding, parse_player, search, get_player_season, parse_squad
from api import AttrDict
import pytest
import json

def test_parse_squad():
    results = parse_squad('390', '79')
    assert len(results) == 28
    player = results[15]
    assert player.player_id == '3055'
    # assert player.season_id == '79'
    # assert player.link == "/wystepy.php?id=3055&amp;id_sezon=79"
    assert player.name == 'Sebastian Mila'
    assert player.apparences == '34'
    assert player.first_squad == '24'
    assert player.substitute == '1'
    assert player.minutes == '2844'
    assert player.yellow_cards == '6'
    assert player.red_cards == '0'
    assert player.goals == '7'
    assert player.own_goals == '0'
    assert player.penalties_scored == '0'
    assert player.penalties_missed == '0' 
    print(player)

@pytest.mark.skip
def test_player_season():
    results = get_player_season('17454', '81')
    assert results.link == 'http://www.90minut.pl/wystepy.php?id=17454&id_sezon=81'
    assert results.season == '2012/13'
    assert len(results.games) == 20
    
    game0 = results.games[0]
    assert game0.hour == '20:45'
    assert game0.date == '2012-07-18'
    assert game0.competition == 'LM, II runda eliminacyjna - I mecz'
    assert game0.host == 'FK Budućnost (Podgorica)'
    assert game0.result == '0-2'
    assert game0.guest == 'Śląsk Wrocław'
    assert game0.number == '21'
    assert game0.play_time == '82-90'

@pytest.mark.skip
def test_search():
    results = search('Cristian Omar Diaz')
    assert 'ZAWODNICY' in results.keys()
    assert 'KLUBY' in results.keys()
    assert 'SĘDZIOWIE' in results.keys()
    assert results['ZAWODNICY']['Cristián Díaz'] == '/kariera.php?id=17454'
    results = search('Bielik')

@pytest.mark.skip
def test_get_first_finding():
    cristian = parse_player('17454')
    cristian2 = get_first_finding('Cristian Omar Diaz')
    assert cristian == cristian2

@pytest.mark.skip
def test_parse_player():
    cristian = parse_player('17454')
    assert cristian['link'] == "/kariera.php?id=17454"
    assert cristian['name'] == 'Cristián Omar (Cristián)'
    assert cristian['birthplace'] == ' San Miguel de Tucumán'
    assert cristian['position']
    assert cristian.position == 'napastnik'
    assert cristian.goals == '15'
    assert cristian.games == '52'
    assert cristian.birthdate == '3 listopada 1986'
    assert cristian.height == '183 cm'
    assert len(cristian.seasons) == 15
    assert len(cristian.seasons[0]) == 8
    assert cristian.seasons[0].season == '2005/06'
    assert cristian.seasons[7].link == '/wystepy.php?id=17454&id_sezon=77'
    assert cristian.seasons[0].country == 'Argentyna'
    assert cristian.seasons[0].club == 'Club Gimnasia y Esgrima de Concepción del Uruguay'
    assert cristian.seasons[0].link_club == '/skarb.php?id_klub=10463&id_sezon=67'
    assert cristian.seasons[7].matches == '18'
    assert cristian.seasons[7].goals == '8'
    assert cristian.seasons[6].trophies[0] == 'król strzelców'
#    print(json.dumps(cristian, indent=4, ensure_ascii=False))


