import sys
input = sys.stdin.readline

# str = list(map(str, input().strip()))
str = input().strip()
# print(str)
cro2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cro3 = ['dz=']
result2, result3 = 0, 0

pin = 0
while (pin < len(str)-2):
    temp = str[pin] + str[pin+1] + str[pin+2]
    if cro3[0] == temp:
        result3 += 1
        str = str[:pin]+str[pin+2:]
    pin += 1


for i in range(len(str)-1):
    temp = str[i] + str[i+1]
    # print(temp)
    for j in cro2:
        if j == temp:
            print(j, temp)
            result2 += 1
# print(result2, result3)
print(len(str)-result2)

