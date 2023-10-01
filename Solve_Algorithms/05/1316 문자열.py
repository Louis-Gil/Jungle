import sys
input = sys.stdin.readline
num = int(input())
str_lst = []

result = 0
temp_lst = []

for i in range(num):
    str_lst =input().strip()
    temp_lst = str_lst[0]

    for j in range(1, len(str_lst)):
        if str_lst[j] == temp_lst[-1]:
            continue
        if str_lst[j] in temp_lst:
            break
        temp_lst+=str_lst[j]
    else :
        result += 1
print(result)


