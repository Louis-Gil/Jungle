N, M = list(map(int, input().split()))
tmp = []

def NM2(N, M, start):
    if len(tmp) == M :
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(start, N+1):
        if i not in tmp:
            tmp.append(i)
            NM2(N, M, i+1)
            tmp.pop()

NM2(N, M, 1)