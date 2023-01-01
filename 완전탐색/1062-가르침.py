# https://www.acmicpc.net/problem/1062
import sys   
import itertools
input = sys.stdin.readline 

n, m = map(int, input().split())
words = [(input()[4:-5]) for _ in range(n)]
# print(words)
alpha = set('antic')
m -= len(alpha)

if m < 0:
    print(0)
    exit()
if m == 21:
    print(n)
    exit()

letters = []
for i in range(26):
    if chr(i + 97) not in alpha:
        letters.append(chr(i + 97))

res = 0
combs = itertools.combinations(letters, m)
for comb in combs:
    cnt = 0
    for word in words:
        for char in word:
            if char not in comb and char not in alpha:
                break
        else:
            cnt += 1
        res = max(cnt, res)

print(res)