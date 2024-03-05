# https://school.programmers.co.kr/learn/courses/30/lessons/42895
def solution_dp_1(N, number):
	if N == number:
		return 1

	s = [set() for _ in range(8)]

	for index, value in enumerate(s, start=1):
		value.add(int(str(N) * index))

	for i in range(1, 8):
		for j in range(i):
			for op1 in s[j]:
				for op2 in s[i-j-1]:
					s[i].add(op1 + op2)
					s[i].add(op1 - op2)
					s[i].add(op1 * op2)

					if op2 != 0:
						s[i].add(op1 // op2)
		if number in s[i]:
			answer = i + 1
			break
	else:
		answer = -1

	return answer

# print(solution_dp_1(5, 12)) # 4


# https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution_dp_2(triangle):
	def dp(max_high, next_list):
		next_high = []
		for i in range(len(next_list)):
			if i == 0:
				next_high.append(max_high[0] + next_list[i])
			elif i == len(next_list) - 1:
				next_high.append(max_high[i-1] + next_list[i])
			else:
				next_high.append(max(max_high[i-1], max_high[i]) + next_list[i])
		return next_high

	max_high = triangle[0]
	for i in range(len(triangle) - 1):
		max_high = dp(max_high, triangle[i+1])
	return max(max_high)

# print(solution_dp_2([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30


# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution_dp_3(m, n, puddles):
    ways = [[-1] * (m+1) for _ in range(n+1)]

    for puddle in puddles:
        ways[puddle[1]][puddle[0]]=0

    check=False
    for i in range(1,n+1):
        if ways[i][1]==0: check=True

        if check: ways[i][1]=0
        else: ways[i][1]=1

    check=False
    for i in range(1,m+1):
        if ways[1][i]==0: check=True

        if check: ways[1][i]=0
        else: ways[1][i]=1

    for i in range(2,n+1):
        for j in range(2,m+1):
            if ways[i][j]==0: continue
            else:
                ways[i][j]=ways[i-1][j]+ways[i][j-1]

    return ways[-1][-1]%1000000007
	
# print(solution_dp_3(4, 3, [[2, 2]])) # 4


# https://school.programmers.co.kr/learn/courses/30/lessons/1843
def solution_dp_4(arr):
    M = [0, 0, 0]
    m = [0, 0, 0]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == '-':
            M = [i - temp for i in M]
            m = [i - temp for i in m]
            if i != 1:
                M = [-max(M + m), max(M + m), max(M + m)]
                m = [-min(M + m), min(M + m), min(M + m)]
            else:
                result = max(M + m)
        elif arr[i] == '+':
            M = [M[0] - temp, M[1] - temp, M[2] + temp]
            m = [m[0] - temp, m[1] - temp, m[2] + temp]
            if i == 1:
                result = M[2]
        else:
            temp = int(arr[i])
    result += temp
    return result

# print(solution_dp_4(["5", "-", "3", "+", "1", "+", "2", "-", "4"])) # 3


def solution_dp_5(money):
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(dp1[-2], dp2[-1])

# print(solution_dp_5([1, 2, 3, 1])) # 4