#Juego Piedra papel o tijera
#piedra gana a tijera
#tijera gana a papel
#papel gana a piedra
import random


def jugar():
    usuario = input("""Escoge una opcion:
    'pi' para piedra
    'pa' para papel
    'ti' para tijera \n""").lower()

    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'

    if gana_jugador(usuario, computadora):
        return '¡Ganaste!'

    return '¡Perdiste!'


def gana_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti') or (jugador == 'ti' and oponente == 'pa') or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


if __name__ == '__main__':
    print(jugar())

