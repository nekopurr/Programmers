# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    player_dict = {player: i for i, player in enumerate(players)}

    for call in callings:
        idx = player_dict[call]
        players[idx], players[idx-1] = players[idx-1], players[idx]

        player_dict[players[idx]] = idx
        player_dict[players[idx-1]] = idx - 1

    return players

"""
# 시간초과 (index는 순회를 하기 때문에)
def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
    return players
"""