from collections import deque

# https://school.programmers.co.kr/learn/courses/30/lessons/43165
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

# print(solution_dfs_1([1, 1, 1, 1, 1], 3)) # 5
# print(solution_bfs_1([1, 1, 1, 1, 1], 3)) # 5

