import sys
sys.stdin = open('02\input.txt', 'r')
number_num, delete_num = list(map(int, sys.stdin.readline().split()))
Big_num = str(sys.stdin.readline()).rstrip()
result = ""
print(number_num, delete_num, Big_num, result)
# 1924 중 2개 삭제이면 1부터 2까지 탐색하고
# 가장 큰 수 넣고 그 앞 다 지우기
# 만약 여러개면 왼쪽 수

count = 0
for i in range(number_num - delete_num): #최종결과 자리 만큼 반복
    stack = [0, Big_num[0]]
    for j in range(1, len(Big_num)-delete_num+1):#리스트의 [0]부터 차례로 비교, 나중에 수정
        if Big_num[j] > stack[1]:
            stack = [j, Big_num[j]]
    result += stack[1]
    Big_num = Big_num[stack[0]+1:]
    delete_num -=1
print(result)
