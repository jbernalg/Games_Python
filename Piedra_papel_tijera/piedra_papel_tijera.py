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
