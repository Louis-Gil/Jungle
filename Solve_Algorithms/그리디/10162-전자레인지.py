# https://www.acmicpc.net/problem/10162

Num = int(input())

Arr = [300, 60, 10]
result = [0, 0, 0]
if Num % 10 != 0:
    print(-1)
else:
    for i in Arr:
        print(Num//i, end=' ')
        Num = Num%i
    