"""trailing zeros"""
class Solution:
    """solution"""
    def trailing_zeros(self, n):
        """time: log(n)"""
        count = 0

        while n != 0:
            count += n // 5
            n = n// 5

        return count


    
    def trailing_zeros(self, n):
        count = 0
        start = 5
        while start <= n:
            count += n // start
            start *= 5

        return count