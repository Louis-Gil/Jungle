from itertools import permutations
n = int(input())
k = int(input())
arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr_per = []
# for i in permutations(arr, k):
#     arr_per.append(i)


check = [0] * len(arr)
def perm(arr, k):
    result = []
    if k == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in perm(arr[:i] + arr[i+1:], k-1):
            result.append([elem] + rest)
    return result


arr_per = perm(arr, k)
temp_arr = []
for i in range(len(arr_per)):
    temp = ''
    for j in range(len(arr_per[i])):
        temp = temp + arr_per[i][j]
    temp_arr.append(temp)
temp_arr = list(set(temp_arr))
print(len(temp_arr))