import sys
input = sys.stdin.readline

coin_num, target = map(int,input().split())
coin_lst = []
for i in range(coin_num):
    coin_lst.append(int(input()))
# print(coin_num, target, coin_lst)

result = 0
for i in coin_lst[::-1]:
    if target >= i:
        result += target//i
        target = target%i
    if target == 0:
        break
print(result)