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

## from collections import defaultdict

graph = defaultdict(list)
def add_edge(graph, u, v):
  graph[u].append(v)

add_edge(graph, 'A', 'B')

for vertex, edges in graph.items():
  print(f"{vertex}: {edges}")

## import heapq

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)

small1 = heapq.heappop(heap)
small2 = heapq.heappop(heap)
print(small1, small2)
