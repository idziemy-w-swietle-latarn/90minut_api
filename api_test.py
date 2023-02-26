from api import get_first_finding

def test_get_first_finding():
    cristian = get_first_finding('Cristian Omar Diaz')
    assert cristian['link'] == "/kariera.php?id=17454"
    assert cristian['name'] == 'Cristián Omar (Cristián)'
    assert cristian['birthplace'] == ' San Miguel de Tucumán'
    assert cristian['position']
    assert cristian.position == 'napastnik'
    assert cristian.goals == '15'
    assert cristian.games == '52'
    assert cristian.birthdate == '3 listopada 1986'
    assert cristian.height == '183'
    assert cristian.first_club == 'Club Gimnasia y Esgrima de Concepción del Uruguay'