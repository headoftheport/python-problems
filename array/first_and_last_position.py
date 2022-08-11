class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end, mid = -1, -1, -1
        i = 0 
        j = len(nums) - 1
        found = False
        while(i<=j):
            mid = (i + j) // 2
            
            if nums[mid] == target:
                found = True
                break
            
            if nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        
        if not found:
            return [start, end]
        
        print(mid, i, j)        
        start = mid
        end = mid
        
        while i<start:
            mid = (i + start) // 2
            if mid == start:
                break
                
            if nums[mid] == target:
                start = mid
            else:
                i = mid+1
        print(start) 
        
        while j>end:
            mid = (j + end + 1) // 2
            if mid == end:
                break
            if nums[mid] == target:
                end = mid
            else:
                j = mid-1
           
        return [start, end]

    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(low, high):
            
            if nums[low] == target == nums[high]:
                return [low, high]
            if nums[low] <= target <= nums[high]:
                mid = (low + high)//2
                l,r = search(low, mid), search(mid+1,high)
                return max(l,r) if -1 in l+r else [l[0],r[1]]
            return [-1,-1]
        
        if len(nums) == 0:
            return [-1,-1]
        
        return search(0, len(nums)-1)
        
    
        