from src.blackjack import asignar_valor_carta, calcular_puntos, determinar_ganador

def test_asignar_valor_carta():
    assert asignar_valor_carta("2", 0) == 2
    assert asignar_valor_carta("A", 10) == 1
    assert asignar_valor_carta("A", 5) == 11
    assert asignar_valor_carta("K", 0) == 10

def test_calcular_puntos():
    assert calcular_puntos(["2", "5", "A"]) == 18
    assert calcular_puntos(["K", "A"]) == 21
    assert calcular_puntos(["A", "A", "A"]) == 13

def test_determinar_ganador():
    assert determinar_ganador(22, 22, "Jugador1", "Jugador2") == "Game over ¡Los dos os habéis pasado!"
    assert determinar_ganador(18, 18, "Jugador1", "Jugador2") == "¡Empate!"
    assert determinar_ganador(15, 22, "Jugador1", "Jugador2") == "¡Gana Jugador1!"
    assert determinar_ganador(20, 18, "Jugador1", "Jugador2") == "¡Gana Jugador1!"
    assert determinar_ganador(17, 20, "Jugador1", "Jugador2") == "¡Gana Jugador2!"