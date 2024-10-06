from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min = float('inf')
        max_profit = 0
        for iterator, price in enumerate(prices):
            if iterator+1 == len(price):
                break
            current_price = prices[iterator+1]
            current_profit = min - current_price
            if current_profit> max_profit:
                max_profit = current_profit
            if price<min:
                min = price
            
                
        return max_profit
            
        
            