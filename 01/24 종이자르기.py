import sys

# sys.stdin = open('01\input.txt', 'r')

a = list(map(int, sys.stdin.readline().split()))
# print(a)
slice_row = [0]
slice_col = [0]

b = int(sys.stdin.readline())
c = []
for _ in range(b):
    c = list(map(int, sys.stdin.readline().split()))
    # print(c)
    slice_num = c[1]
    if (c[0] == 1) & ( 0 < slice_num < a[0]): #가로
        slice_row.append(slice_num)
        slice_row.sort()        
    elif (c[0] == 0) & ( 0 < slice_num < a[1]) : #세로
        slice_col.append(slice_num)
        slice_col.sort()

slice_row.append(a[0])
slice_col.append(a[1])

# print(slice_row)
# print(slice_col)

result = []
for i in range(len(slice_row)-1):
    for k in range(len(slice_col)-1):
        area = (slice_row[i+1] - slice_row[i]) * (slice_col[k+1] - slice_col[k])
        result.append(area)

# print(result)
print(max(result))