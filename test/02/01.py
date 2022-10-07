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

# 아마 temp 설정이 잘못 되어서 시간초과 또는 틀린 것 같습니다.
# temp가 기존 s가 아니라 'm'+'o'*(k+2) 가 되어야 맞을 것 같습니다