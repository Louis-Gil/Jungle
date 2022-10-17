import sys
input = sys.stdin.readline

word = str(input().strip())
# print(word)
temp1 = word.split('-')
# print(temp1)
num = []

for i in temp1:
    cnt = 0
    temp2 = i.split('+')
    for j in temp2:
        cnt += int(j)
    num.append(cnt)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)