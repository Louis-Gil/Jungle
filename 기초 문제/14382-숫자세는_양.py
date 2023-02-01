# https://www.acmicpc.net/problem/14382
import sys
input = sys.stdin.readline

def simulation(num):
    number_set = set()
    i = 1
    while True:
        if i > 100:
            break
        number_set = number_set | set(str(num*i))
        if len(number_set) == 10:
            return str(num*i)
        i += 1
    return 'INSOMNIA'

T = int(input())
for test_case_num in range(1, T+1):
    N = int(input())
    print(f'Case #{test_case_num}: {simulation(N)}')