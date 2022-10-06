# 테스트 케이스 통과
# 시간 초과

import sys

input = sys.stdin.readline

string = input().strip()

bomb = input().strip()


def bomb_string(string, bomb):
    while bomb in string:
        string = string.replace(bomb, "")
        if not string:
            return "FRULA"

    return string


print(bomb_string(string, bomb))