# 시간초과 - 유니온 파인드
import sys
input = sys.stdin.readline

Gates = int(input())
Planes = int(input())

Landing = [0] * (Gates+1)
result = 0
flag = 1
planes_list  = []
for _ in range(Planes):
    planes_list.append(int(input().strip()))
    
for plane in planes_list:
    if flag == 0 :
        break
    
    for i in range(plane, 0, -1):
        if Landing[i] == 0:
            result += 1
            Landing[i] = 1
            break
    else :
        flag = 0


print(result)
    
    
    
# #
# import sys

# g = int(sys.stdin.readline().rstrip())

# p = int(sys.stdin.readline().rstrip())

# count = 0

# gate_list = [0 for _ in range(g)]
# plane_list = []
# for i in range(p):
#     plane_list.append(int(sys.stdin.readline().rstrip()))

# # 비행기가 순서대로 도착하는데 도킹못하면 폐쇄됨.
# for i in plane_list:
#     p_idx = i-1
#     if sum(gate_list) == len(gate_list):  # 게이트에 비행기가 가득찬 경우 종료
#         break

#     if gate_list[p_idx] == 0:  # 비행기 번호에 맞는 게이트가 비어있으면 집어넣는다.
#         gate_list[p_idx] = 1
#     else:  # 비행기 번호에 맞는 게이트가 이미 채워져 있다면
#         for j in range(p_idx, -1, -1):  # 최대한 큰 번호의 게이트에 비행기를 넣는다. (비행기 번호보다는 작거나 같은 게이트여야 함)
#             if gate_list[j] == 0:
#                 gate_list[j] = 1
#                 break
#             break

# print(sum(gate_list))
# #print("도착한 비행기 순서", plane_list)
# #print("게이트: ", gate_list)