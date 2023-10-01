import sys
input = sys.stdin.readline

arr = []
result = [-1,0,0]
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if result[0] < arr[j]:
            result = [arr[j], i+1, j+1]
print(result[0])
print(result[1], result[2])