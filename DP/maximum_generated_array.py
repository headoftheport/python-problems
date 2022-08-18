"""maximum in generated array"""
class Solution:
    """solution"""
    def maximum_generated_array(self, n):
        """iterative solution"""
        #time complexity: O(n)
        #space complexity: O(n)
        if n == 0:
            return 0
        
        if n == 1:
            return 1        
        it = 1
        store = [0 for i in range(n+1)]
        store[0] = 0
        store[1] = 1
        
        while True:
            if it * 2 <= n:
                store[it*2] = store[it]
            else:
                break
                
            if (it * 2) + 1 <= n:
                store[(it * 2) + 1] = store[it] + store[it+1]
            else:
                break
                
            it = it + 1
            
        return max(store)


    def maximum_generated_array2(self, n):
        """iterative solution"""
        if n < 2:
            return n

        store = [0] * (n+1)
        store[0] = 0
        store[1] = 1
        maxValue = 1
        for i in range(2, n+1):
            store[i] = store[(i//2)]
            if i % 2 != 0:
                store[i] += store[(i//2) + 1]
            maxValue = max(maxValue,store[i])
            
        return maxValue
