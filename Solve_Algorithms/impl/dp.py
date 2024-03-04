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