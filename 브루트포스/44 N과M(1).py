N, M = list(map(int, input().split()))
result = []

def NM1(N, M):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            NM1(N, M)
            result.pop()
NM1(N, M)