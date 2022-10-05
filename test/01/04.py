import sys
input = sys.stdin.readline

m, d = map(int, input().split())

month_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_arr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def solution(m, d):
    temp = (sum(month_arr[:m-1]) + d - 1) % 7
    return week_arr[temp]

print(solution(m, d))