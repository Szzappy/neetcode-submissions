class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = 0
        for i in range(len(prices)):
            if prices[i] < prices[start]:
                start = i
            
            elif prices[i] > prices[start]:
                temp_profit = prices[i] - prices[start]

                if temp_profit > profit:
                    profit = temp_profit
        
        return profit

