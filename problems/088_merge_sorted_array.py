from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    p1 = m - 1      # Pointer for nums1 valid elements
    p2 = n - 1      # Pointer for nums2 elements
    p = m + n - 1   # Insertion pointer at the end of nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Place any remaining elements from nums2 into nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


def main() -> None:
    # Test Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Merged Array 1: {nums1}")
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Expected [1, 2, 2, 3, 5, 6], got {nums1}"

    # Test Case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(f"Merged Array 2: {nums1}")
    assert nums1 == [1], f"Expected [1], got {nums1}"

    # Test Case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"Merged Array 3: {nums1}")
    assert nums1 == [1], f"Expected [1], got {nums1}"

    print("All test cases for Problem 88 passed!\n")


if __name__ == "__main__":
    main()