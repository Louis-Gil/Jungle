def is_promising(x):
    for i in range(x):
        if border[x] == border[i] or abs(border[x] - border[i]) == abs(x - i):
            return False
    return True
def nqueen(x):
    global count
    if x == N:
        count += 1
        return
    else:
        for i in range(N):
            border[x] = i
            if is_promising(x):
                nqueen(x + 1)
    return count
N = int(input())
border = [0] * N
count = 0
print(nqueen(0))