N, M = list(map(int, input().split()))
tmp = []

def NM2(N, M, idx):
    if len(tmp) == M :
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(idx, N+1):
            tmp.append(i)
            NM2(N, M, idx)
            tmp.pop()

NM2(N, M, 1)

