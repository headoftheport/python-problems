class Solution:
    """divisor game - dymanic programming"""
    def divisor_game(self, n: int) -> bool:
        """solution"""

        store = [False for i in range(n+1)]
        for i in range(2,n+1):
            divisor = i // 2
            while divisor > 0:
                if i % divisor == 0 and store[i - divisor] == False:
                    store[i] = True
                    break
                divisor = divisor - 1
                    
        
        return store[-1]


print(Solution().divisor_game(3))