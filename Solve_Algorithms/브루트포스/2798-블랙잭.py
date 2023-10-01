# https://www.acmicpc.net/problem/2798
import sys
import itertools

Get_list = list(map(int, sys.stdin.readline().split()))
Num, Max_num = Get_list

card_list = list(map(int, sys.stdin.readline().split()))
card_list.sort()
# print(Num, Max_num, card_list)


def blackjack(card_list, Max_num):
    result = 0
    nPr = list(itertools.combinations(card_list, 3))
    for i in nPr:
        if ((sum(i)) > result) & ((sum(i)) <= Max_num):
            result = sum(i)
    return result



result = blackjack(card_list, Max_num)
print(result)