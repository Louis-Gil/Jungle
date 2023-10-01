import sys
input = sys.stdin.readline

test_num = int(input())
test_lst = list(map(int, input().split()))

# print(test_num, test_lst)
result = 0
temp = 0


for i in test_lst:
    # if i < 1:
    if i< 0 and temp < abs(i):
        temp = 0
        continue
    temp += i
    if result < temp:
        result = temp
if result == 0:
    print(max(test_lst))
else :
    print(result)