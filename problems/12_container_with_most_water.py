height = [1,8,6,2,5,4,8,3,7]
max_water = 0 
n = len(height)

# Brute force O(n^2)
for i in range(n):
    for j in range(i+1, n):
        w = j - i
        ht = min(height[i], height[j])

        area = w * ht
        max_water = max(max_water, area)
print(max_water)