
sum = 0

def calcul(x):
    global sum
    if x == 0:
        sum += 1

    elif x == 1:
        calcul(0)

    elif x == 2:
        calcul(1)
        calcul(0)

    else:
        calcul(x-1)
        calcul(x-2)
        calcul(x-3)

    return sum 

answer = []
for _ in range (int(input())):
    number = int(input())
    calcul(number)
    answer.append(sum)
    sum = 0 

for ans in answer:
    print(ans)