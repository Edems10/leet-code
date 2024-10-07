from typing import List

class Solution1:
    def maxProfit_mine(self, prices: List[int]) -> int:
        profitable_days = {}
        current_price_iterator = 0
        future_price_iterator = 1
        
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

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit

    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
    
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.maxProfit([6, 1, 3, 2, 4, 7])
    print(result)  
