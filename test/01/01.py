import sys

A = list(map(int, sys.stdin.readline().split()))
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0

for i in range(A[0]):
    if i == (A[0]-1):
        result += A[1]
    else :
        result += date[i]
        
if (result % 7) == 1:
    print('MON')
elif (result % 7) == 2:
    print('TUE')
elif (result % 7) == 3:
    print('WED')
elif (result % 7) == 4:
    print('THU')
elif (result % 7) == 5:
    print('FRI')
elif (result % 7) == 6:
    print('SAT')
else : 
    print('SUN')
