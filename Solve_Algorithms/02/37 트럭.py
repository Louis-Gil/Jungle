import sys
from collections import deque
# sys.stdin = open('02\input.txt', 'r')

truck_num, bridge_num, weight_num = map(int, sys.stdin.readline().split())
truck = deque(list(map(int, sys.stdin.readline().split())))

# print(truck_num, bridge_num, weight_num)
# print(truck)
bridge = deque([0]*bridge_num)
time = 0


while bridge:
    time += 1
    bridge.popleft()
    if truck:
        if sum(bridge)+truck[0] <= weight_num:
            bridge.append(truck.popleft())
        else : bridge.append(0)

print(time)