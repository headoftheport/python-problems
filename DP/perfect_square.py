import math


class Solution:
    def __init__(self):
        self.store = {}
        
    def numSquares(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n in self.store:
            return self.store[n]
        
        start = math.floor(math.sqrt(n))
        
        ans = float("inf")
        for i in range(start, 0, -1):
            count = self.numSquares(n - (i*i)) 
            ans = min(ans, count+1)
            
            
            
        self.store[n] = ans 
        return ans
                