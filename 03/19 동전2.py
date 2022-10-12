from collections import deque
import sys
input=sys.stdin.readline

n, value = map(int, input().split())
coins=list(set(int(input()) for _ in range(n)))
check=[0 for _ in range(value+1)] ### 중복된 조합 filter해서 빼주는 효과가 있음// 없으면 메모리 초과난다 ..!
print(check)
def bfs(coins, value):
    queue=deque()
    for coin in coins:
        #코인이 목표보다 높지 않으면 큐에 append
        if coin<value:
            queue.append([coin,1])
            #check 에 코인들 더함
            check[coin]=1

    while queue:
        cum, cnt=queue.popleft()
        if value==cum:
            print(cnt)
            break
        for coin in coins:
            #코인만큼 더하고 / 카운트 만큼 더함
            cum1=cum+coin
            cnt1=cnt+1
            #cum1이 목표보다 낮고, 카운트에 없다면
            if cum1<=value and check[cum1]==0:
                check[cum1]=1
                queue.append([cum1,cnt1])
            
    if cum!=value:
        print('-1')

bfs(coins,value)