height = [1,8,6,2,5,4,8,3,7]
max_water = 0 
n = len(height)

# Brute force O(n^2)
# for i in range(n):
#     for j in range(i+1, n):
#         w = j - i
#         ht = min(height[i], height[j])

#         area = w * ht
#         max_water = max(max_water, area)
# print(max_water)
left = 0
right = n - 1

while(left < right):
    w = right - left
    ht = min(height[left], height[right])
    a = w * ht
    max_water = max(a, max_water)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_water)