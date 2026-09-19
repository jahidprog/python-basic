nums = [2, 2, 1, 1, 3, 3, 5, 6, 6, 7, 7, 5, 8]
ans = 0
# for i in nums:
#     ans ^= i
# print(ans)
n = len(nums)
nums.sort()
# nums = [2, 2, 1, 1, 3, 3, 5, 5, 6, 6, 7, 7, 8]
for i in range(1, n-1, 2):
    if(nums[i] != nums[i-1]):
        ans = nums[i-1]
        break
print(ans)
