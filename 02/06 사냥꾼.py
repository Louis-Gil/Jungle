import sys
# sys.stdin = open('02\input.txt', 'r')

sadae_num, animal_num, rifle = list(map(int, sys.stdin.readline().split()))
sadae = []
animal = []
sadae = list(map(int, sys.stdin.readline().split()))
for _ in range(animal_num):
    animal.append(list(map(int, sys.stdin.readline().split())))

sadae.sort()
# print(sadae_num, sadae, animal_num, animal, rifle)
# print(animal[0][0])

def hunt(sadae, animal, rifle):
    count = 0

# 동물번호가 주어젔을때
# 번호에서 가장 가까운 사대를 찾아서
# 거리에 들어가면 카운트 1
    for i in range(animal_num):
        start = 0
        end = sadae_num-1
        
        while start <= end:
            # <=  <
            mid = ((start + end) // 2)
            
            if animal[i][0] >= sadae[mid] :
                start = mid + 1
                result = mid
                # mid end
                # print('업')
            else : 
                end = mid - 1
                # mid -1    mid
                # print('다운')
        
        if abs(sadae[result] - animal[i][0]) + animal[i][1] <= rifle:
            count += 1
            # print(animal[i])
            break
        # print("다음 번호")
    return count


result = hunt(sadae, animal, rifle)
print(result)