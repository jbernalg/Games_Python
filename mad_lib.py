#Historias locas. Juego

if __name__ == '__main__':
    # org = 'freeCodeCamp'

    # #dar formato a las variables 
    # print('Aprende con {}'.format(org))

    # #usando f-string
    # print(f'Aprende a programar con {org}')

    adj = input('adjetivo: ')
    verbo1 = input('Verbo 1: ')
    verbo2 = input('verbo 2: ')
    sustantivo_plural = input('Sustantivo (Plural): ')

    madlib = f'Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1}. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}' 
    
    print(madlib)
