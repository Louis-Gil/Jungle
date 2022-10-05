import sys
# sys.stdin = open('02\input.txt', 'r')
number_num, delete_num = list(map(int, sys.stdin.readline().split()))
Big_num = str(sys.stdin.readline()).rstrip()
k, stack = delete_num, []
# print(number_num, delete_num, Big_num)

for i in range(number_num): #최종결과 자리 만큼 반복
    while k > 0 and stack and stack[-1] < Big_num[i]:
        stack.pop()
        k -= 1
    stack.append(Big_num[i])
print(''.join(stack[:number_num-delete_num]))

