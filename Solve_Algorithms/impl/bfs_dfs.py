from collections import deque

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