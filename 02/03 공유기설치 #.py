import sys
sys.stdin = open('02\input.txt', 'r')

house_num, IPtime = list(map(int, sys.stdin.readline().split()))
house_list = []
for _ in range(house_num):
    house_list.append(int(sys.stdin.readline()))
house_list.sort()
# print(house_num, IPtime, house_list)

def GongU(house_list, start, end):
    result = 0

    while start <= end:
        count = 1
        mid = (start + end) //2
        current = house_list[0]
        for i in range(1, len(house_list)):
            if house_list[i] >= current + mid:
                count += 1
                current = house_list[i]
        
        if count >= IPtime:
            start = mid + 1
            result = mid
            print('많아요!')
            print(start)
        else :
            end = mid - 1
            print('적어요!')
            print(start)
    return result

start = 1
end = house_list[-1] - house_list[0]
result = GongU(house_list, start, end)
print(result)
