with open('question.txt', 'r') as quesfile, open('answer.txt', 'r') as ansfile:
    
    #almacena las preguntas y respuestas en listas 
    #strip: elimina los espacios innecesarios y nuevas lineas
    questions = [question.strip() for question in quesfile.readlines()]  
    answers = [answer.strip() for answer in ansfile.readlines()]

    #variable para almacenar el puntaje
    score = 0

    # zip. toma iterables como argumentos y devuelve un iterador. 
    # El iterador genera una serie de tuplas que contienen elementos de cada iterable
    for question, answer in zip(questions, answers):  
        user_ans = input(question+' ')

        #verificar si la respuesta es correcta
        if user_ans.lower() == answer.lower():
            print('Correcto!')
            score += 1
        else:
            print('Incorrecto')

    #center. Centra la linea a imprimir
    print(f'Puntuacion Final: {score}/{len(questions)}'.center(100)) 