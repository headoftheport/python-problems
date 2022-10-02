"""solution"""
class Solution:
    """solution"""
    def length_of_lis(self, nums) -> int:
        """
        tabulation
        time: O(n^2)
        space: O(n)
        """
        store = [1 for _ in nums]
        
        for i in range(1,len(nums)):
            j = i - 1
            while j >= 0:
                
                if nums[j] < nums[i]:
                    store[i] = max(store[i], store[j]+1)
                j -= 1
        
        return max(store)


    def length_of_lis2(self, nums) -> int:
        """
        binary search
        time: O(nlogn)
        space: O(max_count)"""
        store = []
        for i in range(len(nums)):
            if len(store) == 0 or store[-1] < nums[i]:
                store.append(nums[i])
            else:
                x = self.left(store, nums[i])
                store[x] = nums[i]
                
        return len(store)
            
    def left(self,store, value):
        """helper"""
        x = 0
        y = len(store)-1
        while x < y:
            mid = (x+y) // 2
            if store[mid] < value:
                x = mid + 1
            else:
                y = mid
                
        return y