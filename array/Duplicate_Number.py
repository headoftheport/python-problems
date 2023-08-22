class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[nums[0]]
        ans = -1
        while slow != fast:
            
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast
    
    def findDuplicate2(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        ans = -1
        while start <= end:
            
            mid = (start + end) // 2
            count = 0
            
            for index, val in enumerate(nums):
                
                if val <= mid:
                    count += 1
                    
            # print(count, mid)
            if count > mid:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
                
        return ans