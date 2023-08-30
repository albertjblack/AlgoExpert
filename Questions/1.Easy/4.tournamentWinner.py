"""
competitions [[home,away]] --> str of len 30
results [winner1, ..., winnern]
results[i] winner of competitions[i] --> 1:homeWin ... 0:awayWin

Assumptions:
- one winner
- at least two teams
- each team faces the other
"""


def tournamentWinner(competitions, results):
    # Write your code here.
    hash_map = {}

    for h, a in competitions:
        hash_map[h] = 0
        hash_map[a] = 0

    for i in range(len(competitions)):
        home = competitions[i][0]
        away = competitions[i][1]
        if results[i] == 1:
            hash_map[home] += 1
        else:
            hash_map[away] += 1

    tmp_winner = competitions[0][0]
    for key, val in hash_map.items():
        if val > hash_map[tmp_winner]:
            tmp_winner = key

    return tmp_winner


if __name__ == "__main__":
    competitions = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = [0, 1, 1]
    winner = tournamentWinner(competitions, results)
    print(winner)
