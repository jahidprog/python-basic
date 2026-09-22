nums = [2, 0, 1, 0, 2, 0, 1, 1, 0, 2, 2, 2,0,2,1,1,0]

cn0, cn1, cn2 = 0, 0, 0
for i in range(len(nums)):
    if nums[i] == 0:
        cn0 += 1
    elif nums[i] == 1:
        cn1 += 1
    else:
        cn2 += 1

idx = 0
for i in range(cn0):
    nums[idx] = 0
    idx += 1
for i in range(cn1):
    nums[idx] = 1
    idx += 1
for i in range(cn2):
    nums[idx] = 2
    idx += 1

print(nums)