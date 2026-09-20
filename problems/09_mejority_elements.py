nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]

cnt = 0
ans = 0

for i in range(len(nums)):
    if cnt == 0:
        ans = nums[i]
    if ans == nums[i]:
        cnt += 1
    else:
        cnt -= 1
print(ans)


