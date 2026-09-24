# 3Sum - Brute Force O(n^3)
# def three_sum(nums):
#     n = len(nums)
#     ans = []
#     s = set()

#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1,n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     trip = [nums[i], nums[j], nums[k]]
#                     trip.sort()
#                     trip = tuple(trip)

#                     if trip not in s:
#                         s.add(trip)
#                         ans.append(list(trip))
#     return ans


# 3Sum - O(n^2)
# def three_sum(nums):
#     n = len(nums)
#     ans = []
#     unique_s = set()

#     for i in range(n):
#         target = -nums[i]
#         s = set()

#         for j in range(i+1, n):
#             third = target - nums[j]

#             if third in s:
#                 trip = [nums[i], nums[j], third]
#                 trip.sort()
#                 trip = tuple(trip)

#                 if trip not in unique_s:
#                     unique_s.add(trip)
#                     ans.append(list(trip))
#             s.add(nums[j])
#     return ans

#  Optimal solution using 2 pointer

def three_sum(nums):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                trip = [nums[i], nums[j], nums[k]]
                ans.append(trip)
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1

            elif sum < 0:
                j += 1
            else:
                k -= 1
    return ans


def main():
    nums = [-1, 0, 1, 2, -1, -4]

    result = three_sum(nums)

    print("Input:", nums)
    print("Three Sum:", result)


if __name__ == "__main__":
    main()
