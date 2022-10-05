import sys
# sys.stdin = open('01\input.txt', 'r')

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
# print(A, B)

n=0
count =0
while n < (len(A)-len(B)+1):
    if A[n:n+len(B)] == B:
        count += 1
        n += (len(B)-1)
    n +=1
print(count)