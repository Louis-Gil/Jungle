import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = a * b * c
d = str(d)

num = [0,0,0,0,0,0,0,0,0,0]

for i in d:
    num[int(i)] += 1

for i in num:
    print(i)

# count(i)
# list(map(int, str(num)))