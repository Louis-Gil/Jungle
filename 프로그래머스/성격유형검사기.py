def solution(survey, choices):
    answer = ''
    cnt = len(choices)
    
    arr = [0 for _ in range (4)]
    for i in range(cnt):
        tmp = survey[i][0]
        if tmp == 'R':
            arr[0] += (choices[i]-4)
        elif tmp == 'C':
            arr[1] += (choices[i]-4)
        elif tmp == 'J':
            arr[2] += (choices[i]-4)
        elif tmp == 'A':
            arr[3] += (choices[i]-4)
        elif tmp == 'T':
            arr[0] -= (choices[i]-4)
        elif tmp == 'F':
            arr[1] -= (choices[i]-4)
        elif tmp == 'M':
            arr[2] -= (choices[i]-4)
        else: # tmp == 'N':
            arr[3] -= (choices[i]-4)
    
    jipyo = [['R','T'], ['C','F'], ['J','M'], ['A','N']]
    for i in range(4):
        if arr[i] <= 0:
            answer += jipyo[i][0]
        else:
            answer += jipyo[i][1]
        
    
    
    return answer


result = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
print(result)
