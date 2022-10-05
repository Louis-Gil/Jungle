import sys
from turtle import right
sys.stdin = open('01\input.txt', 'r')

Num = int(sys.stdin.readline())
Get_list = list(map(int, sys.stdin.readline().split()))
Get_list.sort()
print(Num, Get_list)


def chi(Get_list, Num):
    result = 0
    Middle_list = []

    if Num % 2 ==0:

        Left_list = Get_list[:Num//2]
        Right_list = Get_list[:Num//2-1:-1]
        
        tmp = Right_list.pop()
        Middle_list.append(tmp)
        tmp = Left_list.pop()
        Middle_list.append(tmp)
        print(Middle_list, Left_list, Right_list)

        Get_list = [Middle_list[0]]
        for i in range(Num//2-1):
            Get_list.extend([Left_list[i], Right_list[i]])
        Get_list.append(Middle_list[-1])
        print(Get_list)
        
        for i in range(Num-1):
            result += abs(Get_list[i]- Get_list[i+1])

    
    return result




Result = chi(Get_list, Num)
print(Result)

