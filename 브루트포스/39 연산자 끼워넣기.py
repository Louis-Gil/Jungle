import sys
from itertools import permutations
sys.stdin = open('01\input.txt', 'r')
B = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
calc = list(map(int, sys.stdin.readline().split()))
# print(num, cards, calc)

def put_in(cards, calc):
    global max_num, min_num
    
    calc_lst = []
    for i in range(4):
        for j in range(calc[i]):
            calc_lst.append(i)
    calc_lst_per = list(permutations(calc_lst))
    # print(cards, calc_lst_per)

    for j in calc_lst_per:
        A = sub_put_in(cards, j)
        if max_num < A:
            max_num = A
        if min_num > A:
            min_num = A

def sub_put_in(card, calc):
    result = card[0]
    for i in range(len(calc)):
        if calc[i] == 0:
            result += card[i+1]
        elif calc[i] == 1:
            result -= card[i+1]
        elif calc[i] == 2:
            result *= card[i+1]
        else : 
            result //= card[i+1]
    # print(result)
    return result

max_num = -1e9
min_num = 1e9
put_in(cards,calc)
print(max_num)
print(min_num)