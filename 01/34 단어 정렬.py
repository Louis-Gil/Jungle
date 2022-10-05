import sys
sys.stdin = open('01\input.txt', 'r')

num = int(input())
lst = set()

for i in range(num):
    input_str = (sys.stdin.readline()).rstrip()
    lst.add(input_str)
# print(set_lst)

lst = list(lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)