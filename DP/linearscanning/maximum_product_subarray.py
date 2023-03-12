class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prod = 1
        result = float("-inf")
        
        for i in range(len(nums)):
            prod = prod * nums[i]
            result = max(result, prod)
            if prod == 0:
                prod = 1
         
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[len(nums)-i-1]
            result = max(result, prod)
            if prod == 0:
                prod = 1
                
        return result
            
        