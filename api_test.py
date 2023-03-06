from api import get_first_finding, parse_player, search_results
from api import AttrDict
import pytest



@pytest.fixture
def cristian_fxt():
    cristian = AttrDict({
    'link': "/kariera.php?id=17454",
    'birthplace': ' San Miguel de Tucumán',
    'name': 'Cristián Omar (Cristián)',
    'position': 'napastnik',
    'goals' : '15',
    'games' : '52',
    'birthdate' : '3 listopada 1986',
    'height' : '183',
    'first_club' : 'Club Gimnasia y Esgrima de Concepción del Uruguay'
})
    return cristian

cristian = AttrDict({
    'link': "/kariera.php?id=17454",
    'birthplace': ' San Miguel de Tucumán',
    'name': 'Cristián Omar (Cristián)',
    'position': 'napastnik',
    'goals' : '15',
    'games' : '52',
    'birthdate' : '3 listopada 1986',
    'height' : '183',
    'first_club' : 'Club Gimnasia y Esgrima de Concepción del Uruguay'
})

@pytest.mark.xfail
def test_get_first_finding():
    cristian2 = get_first_finding('Cristian Omar Diaz')
    assert cristian == cristian2

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
    assert len(cristian.seasons[0]) == 6
    
def test_search_results():
    result = search_results('Cristian Omar Diaz')