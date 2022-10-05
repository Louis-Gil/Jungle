import sys
num = input()
a = list(map(int, sys.stdin.readline().split()))

maxnum = max(a)
sosu = [2]
for i in range(3, maxnum+1, 2):
    take = max(sosu)
    for k in sosu:

        if i % k ==0:
            break
        if k == take:
            sosu.append(i)


result = 0
for i in a:
    if i in sosu :
        result += 1
print(result)