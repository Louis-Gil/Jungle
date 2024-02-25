## from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

left = stack.popleft()
print(left)
right = stack.pop()
print(right)
print(stack)


## import heapq

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)

small1 = heapq.heappop(heap)
small2 = heapq.heappop(heap)
print(small1, small2)