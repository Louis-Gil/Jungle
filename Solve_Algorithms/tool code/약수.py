def solution(number, limit, power):
    answer = 0

    #number까지 모든 수 확인
    for i in range(1, number+1):
        arr = []
        #약수 확인
        for j in range(1, int(i**(1/2))+1):
            if (i%j == 0):
                arr.append(j)
                if (j != (i//j)):
                    arr.append(j)
        count = len(arr)
        if count > limit:
            count = power
        answer += count


    return answer