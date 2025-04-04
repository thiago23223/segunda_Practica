import string
import random
import operator

def print_zen():
    vocales = "aeiouAEIOU"
    zen_text = """
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """
    lines = zen_text.splitlines()
    for line in lines:
        palabras = line.split()
        if len(palabras) > 1 and palabras [1][0] in vocales:
            print(line)


def longest_title(titles):
    longest = ""
    for title in titles:
        if(len(title) > len(longest)):
            longest = title
    print("El titulo mas largo es : ", longest)

def word_conduct_code(codes):
    word = input("Ingrese una palabra clave : ")
    for line in codes:
        found = False
        i = 0
        while(not found and i < len(line)):
            if line[i:i+len(word)] == word: 
                found=True
                print(line)
            else:
                i += 1

def valid_user():
    numeros = "0123456789"
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    user = input("Ingrese un nombre de usuario: ")
    pos = 0
    number = False
    upper = False
    other_char = False
    if(len(user)>4):
        while(pos < len(user) and not other_char):
            caracter = user[pos]
            if(not number and caracter in numeros):
                number = True
            elif (not upper and caracter in mayusculas):
                upper = True
            elif (caracter not in minusculas and caracter not in mayusculas and caracter not in numeros):
                other_char = True
            pos +=1
    if(number and upper and not other_char):    
        print("El nombre de usuario es valido")
    else:
        print("El nombre de usuario es invalido")

def velocity_clasification():

    velocity = input("Ingrese su teimpo de reaccion en ms: ")
    check = False
    while(not check):
        if(velocity.isnumeric()):
            check = True
        else:
            velocity = input("Ingrese su teimpo de reaccion en ms: ")
    velocity = int(velocity)
    if(velocity < 200):
        print("Categoria : Rapido")
    elif (velocity <= 500):
        print("Categoria: Normal")
    else:
        print("Categoria: Lento")

def mentions_description(descriptions):
    music = 0
    chatting = 0
    entertainment = 0
    for line in descriptions:
        words = line.split()
        for word in words:
            if(word.lower() == 'musica'):
                music += 1
            elif (word.lower() == 'charla'):
                chatting += 1
            elif (word.lower() == 'entretenimiento'):
                entertainment += 1
    print("Menciones de 'musica' : ", music)
    print("Menciones de 'charla' : ", chatting)
    print("Menciones de 'entretenimiento' : ", entertainment)

def discount_code():
    user = input("Ingrese un usuario de maximo 15 caracteres")
    while(len(user)>15):
        print("Se ha excedido de caracteres")
        user = input("Ingrese un usuario de maximo 15 caracteres")
    fecha = input("Ingrese la fecha (año-mes-dia)")
    fecha = fecha.replace("-","")
    cant_char = 30 - len(user) - len(fecha) - 2
    random_char = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(cant_char))
    code = user.upper() + "-" + fecha + "-" + random_char.upper()
    print("Codigo de descuento: " + code)

def is_anagram():
    palabra1 = input("Ingrese la primer palabra : ").lower()
    while( not palabra1.isalpha()):
        print("No ha ingresado una palabra valida")
        palabra1 = input("Ingrese la primer palabra : ").lower()
    palabra2 = input("Ingrese la segunda palabra : ").lower()
    while( not palabra2.isalpha()):
        print("No ha ingresado una palabra valida")
        palabra2 = input("Ingrese la segunda palabra : ").lower()
    if(len(palabra1) != len(palabra2)):
        print("No son anagramas. ")
    else:
        if (sorted(palabra1)) == (sorted(palabra2)):
            print("Son anagramas. ")
        else:
            print("No son anagramas. ")

    
def print_round(round):
    for player,stats in round.items():
        death = "1" if stats["deaths"] == True else "0"
        print(f"{player} : bajas : {stats['kills']} - asistencias : {stats['assists']} - muertes : {death} \n ")

def get_score(item):
        return item[1]['score']

def print_final_ranking(final_score):
    print("Ranking Final :")
    sorted_final_score = dict(sorted(final_score.items(), key=get_score, reverse=True)) #el get score me extrae de cada subdiccionario la puntuacion para ordenar segun ese criterio en el sorted y el reverse= true es para q sea de forma descendente
    for player,stats in sorted_final_score.items():
        print(f"{player} : bajas : {stats['kills']} - asistencias : {stats['assists']} - muertes : {stats['deaths']} - MVPs : {stats['MVPs']} - puntaje : {stats['score']} \n")

def rounds_calculation(rounds):
    final_score = {'Shadow':{'kills':0,'assists':0,'deaths':0,'MVPs':0,'score':0},
                   'Blaze':{'kills':0,'assists':0,'deaths':0,'MVPs':0,'score':0},
                   'Viper':{'kills':0,'assists':0,'deaths':0,'MVPs':0,'score':0},
                   'Frost':{'kills':0,'assists':0,'deaths':0,'MVPs':0,'score':0},
                   'Reaper':{'kills':0,'assists':0,'deaths':0,'MVPs':0,'score':0}}
    for i,round in enumerate(rounds, start=1): #enumerate me va iterando la diciendome por que ronda voy
        print("Ronda ",i," : ")
        best_score = -2
        best_score_player = None
        for player,stats in round.items():
            final_score[player]['kills'] += stats['kills']
            final_score[player]['assists'] += stats['assists']
            score = stats['kills']*3 + stats['assists']*1
            if stats['deaths'] == True:
                final_score[player]['deaths'] += 1
                score -= 1
            final_score[player]['score'] += score
            if score > best_score:
                best_score = score
                best_score_player = player
        print_round(round)
        print("El MVP de la ronda fue : ", best_score_player)
        final_score[best_score_player]['MVPs'] += 1
    print_final_ranking(final_score)
            
            






