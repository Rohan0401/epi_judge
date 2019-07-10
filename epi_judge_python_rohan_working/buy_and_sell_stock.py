from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    min_price = float('inf')
    profit = 0
    for price in prices:
            profit_today = price - min_price
            min_price = min(price, min_price)
            profit = max(profit, profit_today)

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
