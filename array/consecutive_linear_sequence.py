class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0 
        
        sort = sorted(nums)
        
        ret = 1
        count = 1
        
        for i in range(1, len(sort)):
            gap = sort[i] - sort[i-1]
            if gap == 1 :
                count += 1
            elif gap == 0:
                continue
            else:
                count = 1
                
            ret = max(ret, count)
            
        return ret
            
            
        