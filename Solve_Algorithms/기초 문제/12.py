import sys
a = int(sys.stdin.readline())

for k in range(a):
    b = sys.stdin.readline()
    score = 0
    count = 0
    for i in b:
        if i == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)