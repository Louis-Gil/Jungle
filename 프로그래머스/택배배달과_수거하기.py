def solution(cap, n, deliveries, pickups):
    arr = [[0] for i in range(n*2)]
    round = -1
    while((sum(deliveries)+sum(pickups))!=0):
        round = round + 1
        deli = cap
        pick = cap
        # deliveries 높은 수 계산
        for i in range(n-1, -1, -1):
            if (deli>0 and deliveries[i]>0):
                if deli > deliveries[i]:
                    deli = deli-deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] = deliveries[i]-deli
                    deli = 0
                if i>=arr[round][0]:
                    arr[round][0]=i+1
        # pickups 높은 수 계산
        for i in range(n-1, -1, -1):
            if (pick>0 and pickups[i]>0):
                if pick > pickups[i]:
                    pick = pick-pickups[i]
                    pickups[i] = 0
                else :
                    pickups[i] = pickups[i]-pick
                    pick = 0
                if i>=arr[round][0]:
                    arr[round][0]=i+1
    result = 0
    for i in arr:
        result += i[0]*2
                
    return result

print(solution(4, 5, [1,0,3,1,2], [0,3,0,4,0]))