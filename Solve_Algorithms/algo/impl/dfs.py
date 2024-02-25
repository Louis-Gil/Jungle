def dfs(graph:Dict, start:int):
    visited = {i:False for i in graph.keys()} 
    def search(current:int):
        visited[current] = True
        for nxt in graph[current]: 
            if not visited[nxt]: 
                search(nxt)
    search(start)

def solution1(numbers, target):
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

