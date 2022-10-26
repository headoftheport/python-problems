"""power of operation"""
class Solution:
    """solution"""
    def my_pow(self, x, n):
        """recursive
        time : O(logn)
        space : constant
        """
        if n == 0:
            return 1
        if x == 0:
            return 0

        if n < 0:
            n = -n
            x = 1/x

        return self.my_pow(x*x, n // 2) if n % 2 == 0 else x*self.my_pow(x*x, n //2)


    def my_pow_2(slef, x, n):
        """
        iterative
        time: O(logn)
        space: constant
        """
        if n == 0:
            return 1
        if x == 0:
            return 0

        abs_n = abs(n)
        ans = 1
        while abs_n > 0:
            if abs_n & 1 == 1:
                ans *= x
            abs_n >>= 1
            x *= x

        return ans if n > 0 else 1 /ans