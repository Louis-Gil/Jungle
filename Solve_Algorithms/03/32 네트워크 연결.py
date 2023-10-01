# import sys
import heapq
# input = sys.stdin.readline

# house, road = map(int, input().split())
house, road = 7, 12
visit = [False]*(house+1)
road_lst = [[] for _ in range(house+1)]

# for i in range(road):
#     s, e, w = map(int, input().split())
#     road_lst[s].append([w, e])
#     road_lst[e].append([w, s])
# print(house, road, road_lst)

input_text = [[1,2,3],[1,3,2],[3,2,1],[2,5,2],[3,4,4],[7,3,6],[5,1,5],[1,6,2],[6,4,1],[6,5,3],[4,5,3],[6,7,4]]
for i in input_text:
    s, e, w = i
    road_lst[s].append([w, e])
    road_lst[e].append([w, s])

answer = []
cnt = 0
heap = [[0,1]]
while heap:
    if cnt == house:
        break
    w, s = heapq.heappop(heap)
    if not visit[s]:
        visit[s] = True
        answer.append(w)
        cnt += 1
        for i in road_lst[s]:
            if visit[i[1]] == False:
                heapq.heappush(heap, i)

print(sum(answer) - max(answer))