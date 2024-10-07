from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitable_days = {}
        current_price_iterator = 0
        future_price_iterator = 1
        
        # Build dictionary of profitable day pairs
        while current_price_iterator < len(prices):
            current_price = prices[current_price_iterator]
            if current_price_iterator + 1 == len(prices):
                break
            while future_price_iterator < len(prices):
                future_price = prices[future_price_iterator]
                if future_price > current_price:
                    profitable_days[(current_price_iterator, future_price_iterator)] = future_price - current_price
                future_price_iterator += 1
            current_price_iterator += 1
            future_price_iterator = current_price_iterator + 1

        # Calculate total profit by summing all positive price changes
        max_profit = 0

        # Iterate through the prices and calculate the profit whenever there's an increase
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    result = sol.maxProfit([6, 1, 3, 2, 4, 7])
    print(result)  # Expected output: 7 (buy at 1, sell at 3, buy at 2, sell at 7)
