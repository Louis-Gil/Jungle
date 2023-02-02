import sys
sys.stdin = open('02\input.txt', 'r')

num, level_mount = list(map(int, sys.stdin.readline().split()))
character = []
for _ in range(num):
    character.append(int(sys.stdin.readline()))
character.sort()

# print(num, level_mount, character)

def heos(character, level_mount):
    result = 0
    start = character[0]
    end = character[-1] + level_mount
    # print(start, end)

    while start <= end:
        mid = (start + end) // 2
        mount = 0

        for i in range(num):
            temp = mid - character[i]
            if temp > 0:
                mount += temp
                # print(mount)

        if level_mount >= mount :
            start = mid + 1
            result = mid
            # print('업')
        else :
            end = mid -1
            # print('다운')
    return result

result = heos(character, level_mount)
print(result)