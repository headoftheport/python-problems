"""Fraction to recurring decimal"""
class Solution:
    """solution"""
    def ftord(self, numerator, denominator):
        """
            time: log(numerator)
            space: log(numerator)
        """
        if numerator == 0:
            return "0"

        sign = (numerator < 0) == (denominator < 0)
        ans = ""
        if not sign:
            ans += "-"

        num = abs(numerator)
        den = abs(denominator)

        if num < den:
            ans += "0"
        else:
            ans += str(num // den)
            num = num % den
        if num > 0:
            ans += "."
        store = {}
        store[num] = len(ans)

        while num != 0:
            num = num * 10
            ans += str(num // den)
            num = num % den
            if num in store:
                index = store[num]
                ans = ans[:index] + "(" + ans[index:]
                ans += ")"
                break
            else:
                store[num] = len(ans)

        return ans
        
