# https://www.acmicpc.net/problem/1406
import sys

Text = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
tmp_list = []
corser = len(Text)

for _ in range(N):
    command = sys.stdin.readline().strip()
    if command == 'L':
        if corser > 0:
            corser -= 1
    elif command == 'D':
        if corser < len(Text):
            corser += 1
    elif command == 'B':
        if corser > 0:
            Text.pop(corser-1)
            corser -= 1
    else:
        Text.insert(corser, command[2])
        corser += 1

print(''.join(Text))
