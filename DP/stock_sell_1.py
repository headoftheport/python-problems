class Solution:
    def maxProfit(self, prices) -> int:
        
        rest = [ 0 for i in prices ]
        buy = [ 0 for i in prices ]
        sell = [ 0 for i in prices ]
        
        rest[0] = 0
        buy[0] = -prices[0]
        sell[0] = float('-inf')
        
        
        for i in range(1, len(prices)):
            rest[i] = max(rest[i-1], sell[i-1])
            buy[i] = max(buy[i-1], rest[i-1]-prices[i])
            sell[i] = buy[i-1] + prices[i]
            
        return max(rest[len(prices)-1], sell[len(prices)-1])