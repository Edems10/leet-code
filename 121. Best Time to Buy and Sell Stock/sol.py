from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min = float('inf')
        max_profit = 0
        for iterator, price in enumerate(prices):
            if iterator+1 == len(prices):
                break
            current_price = prices[iterator+1]
            if price<min:
                min = price
            current_profit = current_price - min
            if current_profit> max_profit:
                max_profit = current_profit
                
        return max_profit
            
        
            