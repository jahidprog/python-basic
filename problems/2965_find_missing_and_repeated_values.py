from typing import List


def find_missing_and_repeated_values(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    total_elements = n * n
    counts = {}

    # Count frequencies of each element in the grid
    for row in grid:
        for num in row:
            counts[num] = counts.get(num, 0) + 1

    ans = [-1, -1]

    # Find repeated (count == 2) and missing (count == 0) values
    for num in range(1, total_elements + 1):
        if counts.get(num, 0) == 2:
            ans[0] = num
        elif counts.get(num, 0) == 0:
            ans[1] = num

    return ans


def main() -> None:
    # Test Case 1
    grid1 = [[1, 3], [2, 2]]
    result1 = find_missing_and_repeated_values(grid1)
    print(f"Grid: {grid1} -> Result: {result1}")
    assert result1 == [2, 4], f"Expected [2, 4], got {result1}"

    # Test Case 2
    grid2 = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    result2 = find_missing_and_repeated_values(grid2)
    print(f"Grid: {grid2} -> Result: {result2}")
    assert result2 == [9, 5], f"Expected [9, 5], got {result2}"

    print("All test cases for Problem 2965 passed!\n")


if __name__ == "__main__":
    main()