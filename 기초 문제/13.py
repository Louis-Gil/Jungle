import sys
b = int(sys.stdin.readline())
for _ in range(b):
    a = list(map(int, sys.stdin.readline().split()))
    avg = sum(a[1:])/a[0]
    cnt = 0
    for score in a[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / a[0] * 100
    print(f"{rate:.3f}%")