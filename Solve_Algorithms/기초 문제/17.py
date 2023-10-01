import sys
b = int(sys.stdin.readline())
for i in range(b):
    # a = sys.stdin.readline().rstrip()
    a = list(sys.stdin.readline().split())


    p = []
    for i in a[1]:
        i_repeat = str(i) * int(a[0])
        p.append(i_repeat)
    print(*p)


    # for i in s:
    #     i_repeat = str(i) * r
    #     p.append(i_repeat)