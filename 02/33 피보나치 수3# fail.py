import sys
sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())

pib_lst = [1, 1]

if num == 0:
    print(0)
elif num == 1 | 2:
    print(1)
else :
    for i in range(num - 2):
        pib_lst = [pib_lst[1], sum(pib_lst)]
        if pib_lst[0] > 1000000:
            pib_lst[0] = pib_lst[0]%1000000
if pib_lst[1] > 1000000:
    pib_lst[1] = pib_lst[1]%1000000
print(pib_lst[1])