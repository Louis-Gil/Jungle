돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

# print(돌의내구도, 독)
def 독의이름들(돌의내구도, 독):
    # answer = [ 독[i]['이름'] for i in range(len(독))]
    answer = [i['이름'] for i in 독]
    return answer

def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                # answer[answer.index(i['이름'])] = 'fail'
                del answer[answer.index(i['이름'])]
                break
    # return [i for i in answer if i != 'fail']
    return answer

print(독의이름들(돌의내구도, 독))
print(징검다리를건너라(돌의내구도, 독))
# print(징검다리를건너라(돌의내구도.copy(), 독.copy()))
print(돌의내구도)

# 리스트는 값이 바뀜
# remove O(N), del O(1)  