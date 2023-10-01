import sys
input = sys.stdin.readline

n = int(input())

def mooGame(s, added_moo, n):

    prev_s = (s - added_moo) // 2 ## 이전 s의 길이 

    if n <= prev_s: 
        return mooGame(prev_s, added_moo-1, n) ## 맨 앞

    elif n > prev_s + added_moo: ## 맨 뒤
        return mooGame(prev_s, added_moo-1, n - (prev_s + added_moo))

    else: ## 중간
        if n-prev_s == 1:
            return 'm'
        else:
            return 'o'

s = 3
i = 0
while n > s: # 최소 s[k] 구하기
    i += 1
    s = s*2 + (i+3)

print(mooGame(s, i+3, n))