from typing import Tuple, List, Union
import random

Score = Tuple[int, int]
TirResult = int
History = List[str]


assume_et_Tir = lambda: random.choice([0, 1])



#Donc dans le principe, je metterai en place une fonction qui nous update le score à chaque TIR
def update_Score(score: Score, team : str, result : TirResult) -> Score:
    #exactement ici on récupére l'etat  actuel du scor et on le mets à jour selon le ganeant
    teamA, teamB = score
    if team == "A":
        return(teamA + result, teamB)
    else:
        return(teamA, teamB + result)


#Vérification de la victoire - d'une maniére pure qui peut déterminer si un vainqueur peut être déclaré.
def check_victory(score: Score, tir_count: int) -> Union[str, None]:
    teamA, teamB = score
    rappel_tirs = 5 - tir_count
    #J'ai tout essayer pour l faire d'une maniére récursive mais c'est tellement compliquée
    if tir_count >= 5:
        if teamA > teamB:
            return "Equipe A"
        elif teamB > teamA:
            return "Equipe B"
    
    if rappel_tirs == 0 and teamA == teamB:
        return None  # Je refuse l'arret des tirs, et je relance les tirs jusqu'a que quelqu'un arrive à gagner

    if abs(teamA - teamB) > rappel_tirs:
        return "Equipe A" if teamA > teamB else "Equipe B"
    
    return None


def add_history(history: History, tir_count: int, score: Score, tirA: TirResult, tirB: TirResult) -> History:
    #Ajoute un événement à l'historique
    return history + [f"Tir {tir_count} |   Score :     {score[0]}/{score[1]}       (équipe A : {tirA}, équipe B : {tirB})"]



def tir_sequence(tir_count: int, score: Score, history: History) -> Tuple[Score, History, Union[str, None]]:
    #Gère la séquence de tirs de manière récursive
    tirA = assume_et_Tir()
    tirB = assume_et_Tir()
    
    new_score = update_Score(update_Score(score, "A", tirA), "B", tirB)
    new_history = add_history(history, tir_count, new_score, tirA, tirB)
    
    winner = check_victory(new_score, tir_count)
    
    if winner:
        return new_score, new_history, winner
    else:
        return tir_sequence(tir_count + 1, new_score, new_history)


def start_tirs_au_but() -> None:
    #Démarre la simulation de la séance de tirs au but
    initial_score: Score = (0, 0)
    initial_history: History = []
    
    final_score, final_history, winner = tir_sequence(1, initial_score, initial_history)

    for event in final_history:
        print(event)

    print("\n")
    print("\n")
    print(f"Victoire : {winner} avec un Score Final de {final_score}")



start_tirs_au_but()