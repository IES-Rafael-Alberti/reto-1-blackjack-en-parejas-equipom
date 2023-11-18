import random

def asignar_valor_carta(carta, total_puntos):
    """ Se asignan valores numéricos a cada una de las cartas.
    :param carta: cartas que obtiene el jugador.
    :param total_puntos: total del valor de las cartas que tiene el jugador
    :return: valor de la carta
    """
    if carta.isdigit():
        return int(carta)
    elif carta == "A":
        if total_puntos + 11 <= 21:
            return 11
        else:
            return 1
    else:
        return 10

def calcular_puntos(cartas):
    """ Calculo del total de los puntos del jugador.
    :param total_puntos: total de los puntos del jugador.
    :param ases: ases que tiene el jugador
    """
    total_puntos = 0
    ases = 0

    for carta in cartas:
        total_puntos += asignar_valor_carta(carta, total_puntos)
        if carta == "A":
            ases += 1

    while ases > 0 and total_puntos > 21:
        total_puntos -= 10
        ases -= 1

    return total_puntos

def mostrar_cartas_jugador(jugador, cartas):
    """ Función que muestra las cartas del jugador.
    :param jugador: matriz de 3x3 con la información del tablero.
    :param cartas: todas las cartas que ha recibido el jugador.
    """
    puntos = calcular_puntos(cartas)
    print(f"{jugador} - {cartas} ({puntos})")

def pedir_carta(jugador, cartas):
    """ Preguntar al jugador si quiere otra carta o plantarse.
    """
    accion = input(f"{jugador}, ¿Quieres una carta más (s/n)? ").lower()
    if accion == "s":
        cartas.append(random.choice("A234567890JKQ"))

def jugar_ronda(jugador, cartas):
    """ Ejecucion de las tres rondas jugadas por cada jugador.
    """
    ronda = 1
    jugador_se_planta = False

    while calcular_puntos(cartas) < 21 and not jugador_se_planta:
        print(f"\nRONDA {ronda}")
        mostrar_cartas_jugador(jugador, cartas)

        if calcular_puntos(cartas) == 21:
            break

        pedir_carta(jugador, cartas)

        if calcular_puntos(cartas) > 21:
            print(f"{jugador} se pasa de 21. ¡{jugador} pierde!")
        else:
            plantarse = input(f"{jugador}, ¿Quieres plantarte (s/n)? ").lower()
            if plantarse == "s":
                jugador_se_planta = True

        ronda += 1

def determinar_ganador(puntos_jugador1, puntos_jugador2, jugador1, jugador2):
    """ Funcion que decide el gandador del juego.
    :param puntos_jugador1: total de puntos del primer jugador
    :type puntos_jugador1: int
    :param puntos_jugador2: total de puntos del segundo jugador
    :type puntos_jugador2: int
    :param jugador1: primer jugador de blackjack.
    :param jugador2: segundo jugador de blackjackr
    """
    if puntos_jugador1 > 21 and puntos_jugador2 > 21:
        return "Game over ¡Los dos os habéis pasado!"
    elif puntos_jugador1 == puntos_jugador2:
        return "¡Empate!"
    elif puntos_jugador1 > 21:
        return f"¡Gana {jugador2}!"
    elif puntos_jugador2 > 21:
        return f"¡Gana {jugador1}!"
    elif puntos_jugador1 > puntos_jugador2:
        return f"¡Gana {jugador1}!"
    else:
        return f"¡Gana {jugador2}!"

def main():
    print("Bienvenido al Blackjack!")

    modo_juego = int(input("Seleccione el modo de juego:\n1. Dos jugadores.\n2. Un jugador contra la máquina.\n"))

    jugador1 = input("Ingrese el nombre del Jugador 1: ")
    jugador2 = ""

    if modo_juego == 1:
        jugador2 = input("Ingrese el nombre del Jugador 2: ")
    elif modo_juego == 2:
        jugador2 = "Máquina"

    cartas_jugador1 = []
    cartas_jugador2 = []

    for _ in range(2):
        cartas_jugador1.append(random.choice("A234567890JKQ"))
        cartas_jugador2.append(random.choice("A234567890JKQ"))

    jugar_ronda(jugador1, cartas_jugador1)

    if modo_juego == 1:
        jugar_ronda(jugador2, cartas_jugador2)
    else:
        while calcular_puntos(cartas_jugador2) < 17:
            pedir_carta(jugador2, cartas_jugador2)

    print("\nJUEGO TERMINADO")
    mostrar_cartas_jugador(jugador1, cartas_jugador1)
    mostrar_cartas_jugador(jugador2, cartas_jugador2)

    puntos_jugador1 = calcular_puntos(cartas_jugador1)
    puntos_jugador2 = calcular_puntos(cartas_jugador2)

    resultado = determinar_ganador(puntos_jugador1, puntos_jugador2, jugador1, jugador2)
    print(resultado)

if __name__ == '__main__':
    main()