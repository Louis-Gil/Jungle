import sys
# import heapq
# from collections import deque
input = sys.stdin.readline

N = int(input())
N_arr = [[] for _ in range(N+1)]
N_arr[0] = 0
N_arr[1] = 1



def fibonachi(num):
    if N_arr[num] :
        return N_arr[num]
    else:
        N_arr[num] = fibonachi(num-1) + fibonachi(num-2)
        return N_arr[num]

if N < 2:
    print(N)
else : 
    N_arr[2] = 1
    print(fibonachi(N))