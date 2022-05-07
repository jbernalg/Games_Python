#adivina el numero. Juego de usuario - computador
import random


def adivina_numero_computador(x):
    
    print('-------------------------------')
    print('      Bienvenido  al Juego     ')
    print('-------------------------------')
    print(f'Seleccione un numero entre 1 y {x} para que la computadora intente adivinarlo..')

    lim_inf = 1
    lim_sup = x

    respuesta = ''
    while respuesta != 'c':
        #generamos una prediccion
        if lim_inf != lim_sup:
            prediccion = random.randint(lim_inf, lim_sup)
        else:
            prediccion = lim_inf

        respuesta = input(f'''Mi prediccion es {prediccion}. 
Si es muy alta ingresa (A) 
Si es muy baja ingresa (B) 
Si es correcta ingresa (C) 
''').lower()
        
        if respuesta == 'a':
            lim_sup = prediccion - 1
        elif respuesta == 'b':
            lim_inf = prediccion + 1

    print(f'La computadora adivino el numero. Excelente!. El numero es: {prediccion}')


if __name__ == '__main__':
    adivina_numero_computador(20)


