import sys
input = sys.stdin.readline

# lst = list(map(int,input().split()))
Bear_num, sit_apart = map(int, input().split())
Bear = list(map(int,input().split()))

sit_apart -= 1
# print(Bear_num, sit_apart, Bear)

if 1 > Bear[0]-sit_apart:
    start_sit = 1
else :
    start_sit = Bear[0]-sit_apart
    
result = [Bear[0]]
res_list = [[start_sit, Bear[0]+sit_apart]]
# print(res_list)

for i in range(1, Bear_num):
    Bear_customer = Bear[i]

    permission = True
    
    while(permission):
    # bear_customer 와 res_list 확인
        for j in res_list:
            if j[0] <= Bear_customer <= j[1]:
                Bear_customer = j[1]+1
                break
    # 
        else:
            
            result.append(Bear_customer)
            res_list.append([Bear_customer-sit_apart, Bear_customer+sit_apart])
            permission = False

for n in result:
    print(n, end=' ')
print()