nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
mx = nums[0]

# Brute force O(n^2)
# for i in range(n):
#     sum = 0
#     for j in range(i, n):
#         sum += nums[j]
#         mx = max(mx, sum)
# print(mx)

# Kadan's Algo O(n)
sum = 0
for i in range(n):
    sum += nums[i]
    mx = max(sum, mx)
    if sum < 0:
        sum = 0
print(mx)