class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        """
            cyclic sort
            tc: o(n)
            sc: o(1)
        """
        index = 0
        while(index < len(nums)):
            if nums[index] > 0 and nums[index] <= len(nums) and nums[index] != nums[nums[index]-1]:
                temp = nums[index]
                nums[index] = nums[temp-1]
                nums[temp-1] = temp
            else:
                index += 1
                
                
        for i, val in enumerate(nums):
            
            if val != i + 1:
                return i+1
            
            
        return len(nums)+1
        