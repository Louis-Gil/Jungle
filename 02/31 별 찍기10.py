import sys
# sys.stdin = open('02\input.txt', 'r')

num = int(sys.stdin.readline())

def put_star(num):
    if num == 1:
        return ["*"]
    star = put_star(num//3)
    # print(star)
    L = []
    for i in star:
        L.append(i * 3)
    for i in star:
        L.append(i + ' '*(num//3) + i)
    for i in star:
        L.append(i * 3)
    return L

print('\n'.join(put_star(num)))