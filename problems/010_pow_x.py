# Pow(x, n)


def my_pow(x, n):
    if n == 0:
        return 1

    if x == 0:
        return 0

    if x == 1:
        return 1

    if x == -1 and n % 2 == 0:
        return 1

    if x == -1 and n % 2 != 0:
        return -1

    bf = n
    ans = 1

    if n < 0:
        x = 1 / x
        bf = -bf

    while bf > 0:
        if bf % 2 == 1:
            ans *= x

        x *= x
        bf //= 2

    return ans


def main():
    x = 2.0
    n = 10

    result = my_pow(x, n)

    print("x:", x)
    print("n:", n)
    print("Result:", result)


if __name__ == "__main__":
    main()