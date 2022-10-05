import sys
sys.stdin = open('01\input.txt', 'r')

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
# print(list)


def shell(list, num):
    h = 1
    while h < (n // 9):
        h = h*3 + 1
        # h개 떨어진 원소 비교

    while h > 0:
        for i in range(h,num):
            j = i-h
            # j는 i보다 1작은 0으로 시작하며, 1씩 올라감
            tmp = list[i]
            while j >= 0 and list[j] > tmp:
                list[j + h] = list[j]
                # 교환 기능
                j -= h
                # j가 h만큼 떨어짐
            list[j + h] = tmp
            # list를 tmp와 교환
        h //= 3


shell(list, n)
for i in range(n):
    print(list[i])