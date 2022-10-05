import sys
from bisect import  *
sys.setrecursionlimit(10**6)

num = int(input())
circles= []
ans =2
for _ in range(num):
    center , banji=  map(int,sys.stdin.readline().split())
    circles.append([center-banji , center +banji])

circles.sort( key= lambda x:( x[0], -x[1]))

def checking(start_int, end):
    if start_int == num:
        return 0
    elif circles[start_int][1]==end:
        return 1
    elif circles[start_int][1]!=end:
        tmp_int =bisect_left(circles,[circles[start_int][1],]) 
        if circles[tmp_int][0] is not None and circles[tmp_int][0] == circles[start_int][1]:
            return 1* checking(tmp_int,end)
        else:
            return 0
    else:
        return 0

for i in range(num-1):
    if circles[i][0] == circles[i+1][0]:
        if circles[i][1] == circles[i+1][1]:
            ans+=1
        else:
            start_int = bisect_left(circles,[circles[i+1][1],])
            if circles[start_int][0] == circles[i+1][1]:
                if checking(start_int, circles[i][1]) ==1:
                    ans +=2
                else:
                    ans +=1
            else:
                ans+=1
    else:
        ans +=1
print(ans)
        