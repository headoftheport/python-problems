"""solution"""
class Solution:
    """solution"""
    def divide(self, dividend: int, divisor: int) -> int:
        """
        O(32)
        """

        ans = 0
        sign = (dividend < 0 ) == (divisor < 0)
        x = abs(dividend)
        y = abs(divisor)

        if x == pow(2,31) and divisor == -1:
            return pow(2,31)-1
        
        for i in range(31, -1, -1):
            
            if (x >> i) >= y:
                ans += (1<<i)
                x -= (y << i)
        return ans if sign else -ans