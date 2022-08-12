"""Min Cost Climbing Stairs"""
import math

class Solution:
    """solution"""
    def min_cost_climbing_stair(self, cost) -> int:
        """minCostClimbingStairs"""

        #time complexity: O(n)
        #space complexity: O(n)

        if len(cost) == 1:
            return cost[0]
        
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        for i in range(2, len(cost)):
            
            if cost[i] + cost[i-1] > cost[i] + cost[i-2]:
                cost[i] = cost[i] + cost[i-2]
            else:
                cost[i] = cost[i] + cost[i-1]
                
                
        return min(cost[-1], cost[-2])


    def min_cost_climbing_stair_2(self, cost) -> int:
        """recurssion solution"""
        memo = [-1 for i in cost]
        n = len(cost)
        return min(self.helper(cost, n-1, memo), self.helper(cost, n-2, memo))


    def helper(self, cost, n, memo):
        """helper method"""
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return cost[n]
        if memo[n] != -1:
            return memo[n]

        memo[n] = cost[n] + min(self.helper(cost, n-1, memo), self.helper(cost, n-2, memo))
        return memo[n]


    def min_cost_climbing_stair_3(self, cost):
        """2nd iteration"""


        dp = [-1 for i in cost]

        for index, val in enumerate(cost):
            if index < 2:
                dp[index] = val
            else:
                dp[index] = val + min(dp[index-1], dp[index]-2)

        return min(dp[-1], dp[-2])
            

    def min_cost_climbing_stair_4(self, cost):
        """constant space"""
        first = cost[0]
        sec = cost[1]

        for i in range(2, len(cost)):

            acc = cost[i] + min(first, sec)
            sec = first
            first = acc

        return min(first, sec)



        