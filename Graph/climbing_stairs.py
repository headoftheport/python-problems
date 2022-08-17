"""climbing stairs"""
class Solution:
    """solution"""
    def climbing_stairs(self, n) -> int:
        """bottom up solution"""
        #time complexity : O(n)
        #space complexity : O(n)
        if n == 1:
            return 1
        
        if n == 2:
            return 1 + 1
        
        store = [0, 1, 2]
        
        for i in range(3, n+1):
            store.append(store[i-1] + store[i-2])
            
        return store[-1]


    def climbing_stairs2(self, n):
        """constant space"""

        if n == 1:
            return 1
        
        one_before = 2
        two_before = 1

        for i in range(2,n):
            curr = one_before + two_before
            two_before = one_before
            one_before = curr

        return one_before