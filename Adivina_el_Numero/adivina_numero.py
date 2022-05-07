#Adivina el numero . Juego de Usuario
import random


def adivina_numero(x):

    print('----------------------------------')
    print('       Bienvenido al Juego        ')
    print('----------------------------------')
    print('Adivina el numero generado por la Computadora!')

    num_aleatorio = random.randint(1, x) #numero aleatorio entre 1 y x
    
    prediccion = 0

    while prediccion != num_aleatorio:
        #ingresa un numero el usuario
        prediccion = int(input(f'Adivina un numero entre 1 y {x}: '))

        if prediccion < num_aleatorio:
            print('Intentalo nuevamente. Este numero es muy pequeño')
        elif prediccion > num_aleatorio:
            print('Intentalo nuevamente. Este numero es muy grande')
        
    print(f'Felicitaciones! Adivinaste el numero {num_aleatorio} correctamente!')


if __name__ == '__main__':
    adivina_numero(20)

