import sys
sys.stdin = open('test\\02\input.txt', 'r')

num = int(sys.stdin.readline())


S = "moomooomoo"
temp = "moo"
count = 1
len1 = 10
while len1 < num:
    count += 1
    len1 = len1*2 + len(temp)
    temp, S = S, (S+temp+"o"*count+S)
print(S[num-1])