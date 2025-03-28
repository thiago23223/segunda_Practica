def print_round(round,score_list):
    i = 0
    for player,stats in round.items():
        death = "1" if stats["deaths"] == True else "0"
        print(f"{player} : bajas : {stats['kills']} - asistencias : {stats['assists']} - muertes : {death} - puntaje : {score_list[i]} \n ")
        i += 1

def get_score(item):
        return item[1]['score']

def print_final_ranking(final_score):
    print("Ranking Final :")
    sorted_final_score = dict(sorted(final_score.items(), key=get_score, reverse=True)) #el get score me extrae de cada subdiccionario la puntuacion para ordenar segun ese criterio en el sorted y el reverse= true es para q sea de forma descendente
    for player,stats in sorted_final_score.items():
        print(f"{player} : bajas : {stats['kills']} - asistencias : {stats['assists']} - muertes : {stats['deaths']} - puntaje : {stats['score']} - MVPs : {stats['MVPs']}  \n")

def make_final_score(rounds):
    jugadores = list(rounds[0].keys())
    final_score = { jugador: {'kills':0, 'assists':0,'deaths':0,'MVPs':0,'score':0 }
                   for jugador in jugadores}
    return final_score

def rounds_calculation(rounds,final_score):
    for i,round in enumerate(rounds, start=1): #enumerate me va iterando la diciendome por que ronda voy
        print("Ronda ",i," : ")
        best_score = -2
        best_score_player = None
        score_list = []
        for player,stats in round.items():
            final_score[player]['kills'] += stats['kills']
            final_score[player]['assists'] += stats['assists']
            score = stats['kills']*3 + stats['assists']*1
            if stats['deaths'] == True:
                final_score[player]['deaths'] += 1
                score -= 1
            final_score[player]['score'] += score
            score_list.append(score) #obtengo los puntajes de todos los jugadores
            if score > best_score:
                best_score = score
                best_score_player = player
        print_round(round,score_list)
        print("El MVP de la ronda fue : ", best_score_player)
        final_score[best_score_player]['MVPs'] += 1       