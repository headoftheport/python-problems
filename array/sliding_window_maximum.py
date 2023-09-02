from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int) -> List[int]:
        
        deq = deque()
        res = []
        for i in range(k):
            
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            
        res.append(nums[deq[0]])
        
        for i in range(k, len(nums)):
            
            if deq and deq[0] == i-k:
                deq.popleft()
                
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
                
            deq.append(i)
            res.append(nums[deq[0]])
            
        return res
                
        