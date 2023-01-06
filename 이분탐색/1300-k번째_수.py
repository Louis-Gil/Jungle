# https://www.acmicpc.net/problem/1300
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

left = 1
right = n*n

while left <= right :
    mid = (left+right)//2
    
    count=0
    for i in range(1,n+1):
        count+=min(mid//i,n)
    # print(left,right)
    if count >= m:
        right=mid-1
    else:
        left=mid+1
print(left)
