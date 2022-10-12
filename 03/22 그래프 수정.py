import heapq

n = int(input())

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 모든 노드에 대한 진출차수는 0으로 초기화
outdegree = [0] * (n + 1)

# 결과 정보 저장을 위한 result 변수 선언 및 초기화
result = [0] * (n + 1)

# 방향 그래프의 모든 간선 정보를 입력 받기
for i in range(1, n + 1):
    connection = list(map(int, input()))
    
    # 인접행렬에서 인접한 노드들만 graph 리스트에 추가
    for idx, val in enumerate(connection):
        if val == 1:
            graph[idx + 1].append(i)
            outdegree[i] += 1

# 위상 정렬
def topology_sort(n):
    # 큐에 여러 노드가 있을 경우 인덱스가 큰 노드를 먼저 큐에서 빼기 위해 우선순위 큐(heapq) 사용
    # ( 답이 여러 개일 경우 사전 순으로 제일 앞서는 것 출력하기 위해서 )
    heap = []

    # 차수 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if outdegree[i] == 0:
            heapq.heappush(heap, -i)

    while heap:
        # 우선순위 큐를 이용하여 큐에서 인덱스가 가장 큰 노드 꺼내고
        # 해당 노드와 연결된 노드들의 진출 차수 빼기
        # 큐에서 빼낸 노드번호를 인덱스로 result 리스트에 가장 큰 숫자 (n) 저장 
        # 이 과정에서 새롭게 진출 차수가 0이 되는 노드 큐에 삽입
        now = -heapq.heappop(heap)
        result[now] = n

        for connected_node in graph[now]:
            outdegree[connected_node] -= 1
            if outdegree[connected_node] == 0:
                heapq.heappush(heap, -connected_node)

        n -= 1

topology_sort(n)

# 사이클이 돌아서 그래프 번호를 수정할 수 없다는는 노드가 2개 이상이라면 -1 출력
# 사이클이 돌려면 최소 3개의 노드가 서로를 가리키고 있어야하는데 
# 그러면 2개이상의 노드는 진출 차수가 0이 될 수 없어서 큐에 넣을 수 없다.
if result.count(0) > 2:
    print(-1)
else:
    # print(*result[1:])
    print(' '.join(map(str, result[1:])))