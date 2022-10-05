from bisect import bisect_left, bisect_right
from collections import Counter
import sys
sys.stdin = open('02\input.txt', 'r')

card_num = int(sys.stdin.readline())
card_lst = list(map(int, sys.stdin.readline().split()))
card_lst.sort()
find_num = int(sys.stdin.readline())
find_lst = list(map(int, sys.stdin.readline().split()))
# print(card_num, card_lst, find_num, find_lst)
result_lst = []

# 1안
# for i in range(find_num):
#     count = 0
#     temp = bisect_left(card_lst, find_lst[i])
#     for j in card_lst[temp:]:
#         if j == find_lst[i]:
#             count += 1
#         else:
#             break
#     result_lst.append(count)
# print(*result_lst, sep=" ")

# 2안
# for i in range(find_num):
#     count = 0
#     temp1 = bisect_left(card_lst, find_lst[i])
#     temp2 = bisect_right(card_lst, find_lst[i])
#     count = temp2 - temp1
#     result_lst.append(count)
# print(*result_lst, sep=" ")

# 3안
count = Counter(card_lst)
print(count)
print(' '.join(f'{count[i]}' if i in count else '0' for i in find_lst))