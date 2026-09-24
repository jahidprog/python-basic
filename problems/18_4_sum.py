# 4Sum - Brute Force O(n^4)
# def four_sum(nums, target):
#     n = len(nums)
#     ans = []
#     s = set()
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 for l in range(k + 1, n):
#                     if nums[i] + nums[j] + nums[k] + nums[l] == target:
#                         quad = [nums[i], nums[j], nums[k], nums[l]]
#                         quad.sort()
#                         quad = tuple(quad)
#
#                         if quad not in s:
#                             s.add(quad)
#                             ans.append(list(quad))
#
#     return ans


# 4Sum - O(n^3)
# def four_sum(nums, target):
#     n = len(nums)
#     ans = []
#     unique_s = set()
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             s = set()
#
#             for k in range(j + 1, n):
#                 fourth = target - nums[i] - nums[j] - nums[k]
#
#                 if fourth in s:
#                     quad = [nums[i], nums[j], nums[k], fourth]
#                     quad.sort()
#                     quad = tuple(quad)
#
#                     if quad not in unique_s:
#                         unique_s.add(quad)
#                         ans.append(list(quad))
#
#                 s.add(nums[k])
#
#     return ans


# 4Sum - Optimal solution using 2 pointer - O(n^3)

def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            p = j + 1
            q = n - 1

            while p < q:
                total = nums[i] + nums[j] + nums[p] + nums[q]

                if total == target:
                    quad = [nums[i], nums[j], nums[p], nums[q]]
                    ans.append(quad)

                    p += 1
                    q -= 1

                    while p < q and nums[p] == nums[p - 1]:
                        p += 1

                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1

                elif total < target:
                    p += 1

                else:
                    q -= 1

    return ans


def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    result = four_sum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Four Sum:", result)


if __name__ == "__main__":
    main()