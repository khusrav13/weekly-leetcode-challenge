class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float("inf")
        max_profit = 0

        for price in prices:
            potential_profit_today = price - min_price_so_far
            print(f"Price today is {price} and minimum price so far is {min_price_so_far}")
            max_profit = max(max_profit, potential_profit_today)
            min_price_so_far = min(min_price_so_far, price)
        return max_profit
    