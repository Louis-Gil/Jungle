from collections import deque
from collections import defaultdict
import heapq

# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution_bfs_1(numbers, target):
    queue = deque([(0, 0)])
    count = 0

    while queue:
        idx, currentSum = queue.popleft()

        if idx == len(numbers):
            if currentSum == target:
                count += 1
        else:
            queue.append((idx + 1, currentSum + numbers[idx]))
            queue.append((idx + 1, currentSum - numbers[idx]))
    return count

def solution_dfs_1(numbers, target):
    def dfs(numbers, target, idx, values):
        if idx == len(numbers):
            if values == target:
                return 1
            else:
                return 0

        count = 0
        count += dfs(numbers, target, idx + 1, values + numbers[idx])
        count += dfs(numbers, target, idx + 1, values - numbers[idx])
        return count
    
    return dfs(numbers, target, 0, 0)

# print(solution_bfs_1([1, 1, 1, 1, 1], 3)) # 5
# print(solution_dfs_1([1, 1, 1, 1, 1], 3)) # 5


# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution_bfs_2(n, computers):
    def bfs(computers, start, visited):
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            for i in range(len(computers)):
                if computers[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            count += 1
    return count

def solution_dfs_2(n, computers):
    def dfs(computers, start, visited):
        visited[start] = True
        for i in range(len(computers)):
            if computers[start][i] == 1 and not visited[i]:
                dfs(computers, i, visited)

    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            count += 1
    return count

# print(solution_bfs_2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
# print(solution_dfs_2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2


# https://school.programmers.co.kr/learn/courses/30/lessons/1844
def solution_bfs_3(maps):
    def bfs(maps, start, visited):
        queue = deque([start])
        visited[start[0]][start[1]] = 1

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1 and visited[ny][nx] == 0:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    bfs(maps, (0, 0), visited)
    return visited[-1][-1] if visited[-1][-1] != 0 else -1

def solution_dfs_3(maps):
    def dfs(maps, y, x, visited, count):
        visited[y][x] = count
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1 and (visited[ny][nx] == 0 or visited[ny][nx] > count + 1):
                dfs(maps, ny, nx, visited, count + 1)

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dfs(maps, 0, 0, visited, 1)
    return visited[-1][-1] if visited[-1][-1] != 0 else -1

# print(solution_bfs_3([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])) # 11
# print(solution_dfs_3([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])) # 11


# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution_bfs_4(begin, target, words):
    if target not in words:
        return 0

    def can_transform(word1, word2):
        return sum([word1[i] != word2[i] for i in range(len(word1))]) == 1

    def bfs(begin, target, words):
        queue = deque([(begin, 0)]) 
        visited = set([begin])

        while queue:
            current_word, steps = queue.popleft()

            if current_word == target:
                return steps

            for word in words:
                if word not in visited and can_transform(current_word, word):
                    visited.add(word)
                    queue.append((word, steps + 1))

        return 0

    return bfs(begin, target, words)

def solution_dfs_4(begin, target, words):
    if target not in words:
        return 0

    def can_transform(word1, word2):
        return sum([word1[i] != word2[i] for i in range(len(word1))]) == 1

    def dfs(current, target, words, visited, steps):
        if current == target:
            return steps
        
        min_steps = float('inf')
        for word in words:
            if not visited[word] and can_transform(current, word):
                visited[word] = True
                steps_taken = dfs(word, target, words, visited, steps + 1)
                visited[word] = False  # 백트래킹
                if steps_taken:
                    min_steps = min(min_steps, steps_taken)
        
        return min_steps if min_steps != float('inf') else 0

    visited = {word: False for word in words}
    visited[begin] = True

    return dfs(begin, target, words, visited, 0)


# print(solution_bfs_4("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
# print(solution_dfs_4("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4


# https://school.programmers.co.kr/learn/courses/30/lessons/87694
def solution_bfs_5(rectangle, characterX, characterY, itemX, itemY):
    def bfs(start_x, start_y, target_x, target_y, field, visited):
        q = deque()
        q.append([start_x, start_y])
        visited[start_x][start_y] = 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()
            if x == target_x and y == target_y:
                return (visited[x][y] - 1) // 2 
            
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if field[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    field = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    
    # 직사각형 그리기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1

    return bfs(characterX*2, characterY*2, itemX*2, itemY*2, field, visited)

def solution_dijkstra_5(rectangle, characterX, characterY, itemX, itemY):
    def dijkstra(start_x, start_y, target_x, target_y, field):
        q = []
        heapq.heappush(q, (0, start_x, start_y))
        distances = [[float('inf')] * 102 for _ in range(102)]
        distances[start_x][start_y] = 0

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            dist, x, y = heapq.heappop(q)
            if x == target_x and y == target_y:
                return dist // 2

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < 102 and 0 <= ny < 102 and field[nx][ny] == 1:
                    cost = dist + 1
                    if cost < distances[nx][ny]:
                        distances[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))

    field = [[0] * 102 for _ in range(102)]
    
    # 직사각형 그리기 및 경계 설정
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                field[i][j] = 1
    
    # 경계 내부를 0으로 설정하여, 벽을 넘지 않도록 함
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1+1, x2):
            for j in range(y1+1, y2):
                field[i][j] = 0

    return dijkstra(characterX*2, characterY*2, itemX*2, itemY*2, field)

# print(solution_bfs_5([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)) # 17
# print(solution_dijkstra_5([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)) # 17


# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# not recommended
def solution_bfs_6(tickets):
    def bfs(tickets, queue):
        while queue:
            current, route, visited = queue.popleft()
            if all(visited):
                return route

            for i, (src, dest) in enumerate(tickets):
                if not visited[i] and src == current:
                    new_visited = visited[:]
                    new_visited[i] = True
                    queue.append((dest, route + [dest], new_visited))


    tickets.sort()
    queue = deque([("ICN", ["ICN"], [False] * len(tickets))])
    return bfs(tickets, queue)

def solution_dfs_6(tickets):
    def dfs(tickets, visited, route, start, count):
        route.append(start)
        if count == len(tickets):
            return route

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == start:
                visited[i] = True
                result = dfs(tickets, visited, route, tickets[i][1], count + 1)
                if result:
                    return result
                visited[i] = False
        route.pop()

    tickets.sort()
    visited = [False] * len(tickets)
    route = []
    return dfs(tickets, visited, route, "ICN", 0)

# print(solution_bfs_6([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
# print(solution_dfs_6([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]


# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def solution_bfs_7(n, wires):
    def bfs(v, graph, visited):
        queue = deque([v])
        visited[v] = True
        count = 0

        while queue:
            v = queue.popleft()
            count += 1
            for u in graph[v]:
                if not visited[u]:
                    queue.append(u)
                    visited[u] = True
        return count

    graph = [[] for _ in range(n+1)]
    for v, u in wires:
        graph[v].append(u)
        graph[u].append(v)

    answer = 100
    for i in range(n-1):
        visited = [False for _ in range(n+1)]
        v1, v2 = wires[i]
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        visited[v1] = True
        count1 = bfs(v1, graph, visited)
        count2 = n - count1
        answer = min(answer, abs(count1 - count2))

        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer


def solution_dfs_7(n, wires):
    def dfs(v, graph, visited):
        visited[v] = True
        return sum([1] + [dfs(u, graph, visited) for u in graph[v] if not visited[u]])

    graph = [[] for _ in range(n+1)]
    for v, u in wires:
        graph[v].append(u)
        graph[u].append(v)
    
    answer = 100
    for i in range(n-1):
        visited = [False for _ in range(n+1)]
        v1, v2 = wires[i]
        visited[v2] = True
        tmp = abs(dfs(v1, graph, visited) - dfs(v2, graph, visited))
        answer = min(tmp, answer)

    return answer

# print(solution_bfs_7(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3
# print(solution_dfs_7(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3


# https://school.programmers.co.kr/learn/courses/30/lessons/49189
def solution_bfs_8(n, edge):
    def bfs(graph, start, distances):
        queue = deque([start])
        visited = [False] * (n+1)
        visited[start] = True

        while queue:
            v = queue.popleft()
            for u in graph[v]:
                if not visited[u]:
                    queue.append(u)
                    distances[u] = distances[v] + 1
                    visited[u] = True


    graph = defaultdict(list)

    for e, v in edge:
        graph[e].append(v)
        graph[v].append(e)

    distances = [0] * (n+1)
    bfs(graph, 1, distances)

    max_distance = max(distances)
    return distances.count(max_distance)

def solution_dijkstra_8(n, edge):
    def dijkstra(graph, start):
        distances = {vertex: float('inf') for vertex in range(1, len(graph) + 1)}
        distances[start] = 0
        queue = []
        heapq.heappush(queue, [distances[start], start]) # [distance, vertex]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if distances[current_vertex] < current_distance:
                continue
            
            for adjacent, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, [distance, adjacent])

        return distances

    graph = {i: [] for i in range(1, n+1)}
    for e, v in edge:
        graph[e].append((v, 1))
        graph[v].append((e, 1))
    
    distances = dijkstra(graph, 1)
    max_distance = max(distances.values())
    return list(distances.values()).count(max_distance)


# print(solution_bfs_8(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3
# print(solution_dijkstra_8(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3


# https://school.programmers.co.kr/learn/courses/30/lessons/81302
def solution_bfs_9(places):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def bfs(place, start):
        visited = [[False] * 5 for _ in range(5)]
        queue = deque([(*start, 0)])

        while queue:
            y, x, dist = queue.popleft()
            visited[y][x] = True
            if 0 < dist <= 2 and place[y][x] == 'P':
                return True
            if dist > 2:
                break

            for i in range(4):
                ny, nx = y + directions[i][0], x + directions[i][1]
                if 0 <= ny < 5 and 0 <= nx < 5 and place[ny][nx] != 'X' and not visited[ny][nx]:
                    queue.append((ny, nx, dist+1))

        return False

    answer = []
    for place in places:
        found = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(place, (i, j)):
                        found = True
                        break
            if found:
                break
        answer.append(0 if found else 1)
    return answer

def solution_dfs_9(places):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def is_safe(x, y, place):
        return 0 <= x < 5 and 0 <= y < 5 and place[x][y] != 'X'

    def dfs(x, y, place, visited, step):
        if step == 2:
            return True
        
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_safe(nx, ny, place) and not visited[nx][ny]:
                if place[nx][ny] == 'P' or dfs(nx, ny, place, visited, step + 1) == False:
                    return False
        return True

    def search(place):
        visited = [[False] * 5 for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not visited[i][j]:
                    if not dfs(i, j, place, visited, 0):
                        return False
        return True

    answer = [1 if search(place) else 0 for place in places]
    return answer


# print(solution_bfs_9([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])) # [1, 0, 1, 1, 1]
# print(solution_dfs_9([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])) # [1, 0, 1, 1, 1]
