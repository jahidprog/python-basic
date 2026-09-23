# 3Sum - Brute Force O(n^3)
def three_sum(nums):
    n = len(nums)
    ans = []

    s = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    trip = [nums[i], nums[j], nums[k]]

                    trip.sort()
                    trip = tuple(trip)

                    if trip not in s:
                        s.add(trip)
                        ans.append(list(trip))

    return ans


def main():
    nums = [-1, 0, 1, 2, -1, -4]

    result = three_sum(nums)

    print("Input:", nums)
    print("Three Sum:", result)


if __name__ == "__main__":
    main()
# O^2 solution