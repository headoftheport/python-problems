"""kth largest element"""
from random import random, randint


class Solution:
    """solution"""
    def kth_largest(self, nums, k);
        return self.quick_select(nums, 0, len(nums)-1, k)


    def quick_select(self,nums, start, end, k):
        """quick select"""
        pivot = end
        pos = start
        rand = randint(start, end)
        nums[pivot], nums[rand] = nums[rand], nums[pivot]
        for i in range(start, end):
            if nums[i] <= nums[pivot]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

        nums[pivot], nums[pos] = nums[pos], nums[pivot]

        count = end - pos + 1
        if count == k:
            return nums[pos]

        if count < k:
            return self.quick_select(nums, start, pos-1, k-count)

        return self.quick_select(nums, pos+1, end, k)


        
                



        