N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

nums = sorted(nums)

# for i in range(N):
#     print(nums[i])

print(*nums, sep='\n')