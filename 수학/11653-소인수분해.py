# https://www.acmicpc.net/problem/11653
num = int(input())
soinsu = []

def solve(num):
    if num == 1:
        return
    elif num == 2:
        print(2)
        return
    
    temp = 2
    division = num
    
    while(division%temp == 0):
        division = division//temp
        print(temp)
    temp += 1
    
    # while(temp<=num):
    while temp*temp <= num:
        # print(temp, int(num/2))
        # temp가 나누어 떨어지는지 찾아서 소인수 확인
        if (division%temp):
            temp+=2
            continue
        division = division//temp
        print(temp)
    
    if division > 2:
        print(division)
        

solve(num)
