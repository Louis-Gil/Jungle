# https://www.acmicpc.net/problem/1541
word = input().split('-')
result_lst = []

for i in word:
    nums = i.split('+')
    temp = 0
    for j in nums:
        temp += int(j)
    result_lst.append(temp)
    
result = result_lst[0]
for i in range(1, len(result_lst)):
    result -= result_lst[i]
print(result)