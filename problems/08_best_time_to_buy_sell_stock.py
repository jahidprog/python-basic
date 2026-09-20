def max_profit(prices):
    best_buy = prices[0]
    max_profit_value = 0

    for i in range(1, len(prices)):
        if prices[i] > best_buy:
            max_profit_value = max(
                max_profit_value,
                prices[i] - best_buy
            )

        best_buy = min(prices[i], best_buy)

    return max_profit_value


def main():
    prices = [7, 1, 5, 3, 6, 4]

    result = max_profit(prices)

    print("Prices:", prices)
    print("Maximum Profit:", result)


if __name__ == "__main__":
    main()