N, M = list(map(int, input().split()))
tmp = []

def NM2(N, M):
    if len(tmp) == M :
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(1, N+1):
            tmp.append(i)
            NM2(N, M)
            tmp.pop()

NM2(N, M)
