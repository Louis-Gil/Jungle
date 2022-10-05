import sys
# sys.stdin = open('02\input.txt', 'r')

lan_num, cut_count = map(int, sys.stdin.readline().split())
lan_lst = []
for i in range(lan_num):
    lan_lst.append(int(sys.stdin.readline()))

max_num = max(lan_lst)
# print(lan_lst, cut_count)

start = 1
end = max_num
result = 0

while start <= end:
    mid = (start + end)//2
    temp = 0
    for i in lan_lst:
        temp += i//mid
    
    if temp >= cut_count:
        start = mid+1
        result = mid
    else :
        end = mid-1
    
print(result)