import pytest
from typing import Tuple, List, Union
from unittest.mock import patch


Score = Tuple[int, int]
TirResult = int
History = List[str]


def update_Score(score: Score, team : str, result : TirResult) -> Score:
    teamA, teamB = score
    if team == "A":
        return(teamA + result, teamB)
    else:
        return(teamA, teamB + result)


def check_victory(score: Score, tir_count: int) -> Union[str, None]:
    teamA, teamB = score
    rappel_tirs = 5 - tir_count
    if tir_count >= 5:
        if teamA > teamB:
            return "Equipe A"
        elif teamB > teamA:
            return "Equipe B"
    
    if rappel_tirs == 0 and teamA == teamB:
        return None

    if abs(teamA - teamB) > rappel_tirs:
        return "Equipe A" if teamA > teamB else "Equipe B"
    
    return None


def add_history(history: History, tir_count: int, score: Score, tirA: TirResult, tirB: TirResult) -> History:
    return history + [f"Tir {tir_count} |   Score :     {score[0]}/{score[1]}       (équipe A : {tirA}, équipe B : {tirB})"]


def test_update_score_team_A():
    score = (0, 0)
    result = update_Score(score, "A", 1)
    assert result == (1, 0)


def test_update_score_team_B():
    score = (1, 0)
    result = update_Score(score, "B", 2)
    assert result == (1, 2)


def test_check_victory_equipe_A():
    score = (3, 0)
    score2 = (3, 5)
    result = check_victory(score, 3)
    assert result == "Equipe A"
    result2 = check_victory(score2, 5)
    assert result2 == "Equipe B"



def test_check_victory_equipe_B():
    score = (3, 5)
    result = check_victory(score, 5)
    assert result == "Equipe B"


def test_check_no_victory():
    score = (3, 3)
    result = check_victory(score, 5)
    assert result is None


def test_add_history():
    history = []
    score = (1, 0)
    new_history = add_history(history, 1, score, 1, 0)
    assert len(new_history) == 1
    assert "Tir 1" in new_history[0]
    # assert "Score : 1 / 0" in new_history[0]


#J'arrive pas à tester cette fonction, enft à 3.0 l'equipe A gagne mais je trouve une incohérence entre les TIR et les But
@patch('random.choice', side_effect=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
def test_tir_sequence_victory(mock_random):
    from League_des_Cheampions import tir_sequence
    initial_score = (0, 0)
    initial_history = []
    tir_count = 1
    score, history, winner = tir_sequence(tir_count, initial_score, initial_history)
    assert winner == "Equipe A"
    assert score == (5, 0)  # L'équipe A gagne après 5 tirs
    assert len(history) == 5  # 5 événements dans l'historique

