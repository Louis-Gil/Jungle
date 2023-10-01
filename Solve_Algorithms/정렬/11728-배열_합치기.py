# https://www.acmicpc.net/problem/11728
import sys

N,M = sys.stdin.readline().split()
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

answer_list = A + B
answer = ' '.join(map(str, sorted(answer_list)))
print(answer)