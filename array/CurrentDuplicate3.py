"""current duplicate 3"""
class Solution:
    """solution"""
    def contains_nearby_almost_duplicate(self, nums, indexDiff, valueDiff) -> bool:
        """
        using buckets of size valueDiff
        time: O(n)
        space: O(k)"""
        store = {}
        for index, val in enumerate(nums):
            m = val if valueDiff == 0 else val // (valueDiff + 1)
            if m in store:
                return True
            if m-1 in store and val - store[m-1] <= valueDiff:
                return True
            if m+1 in store and store[m+1] - val <= valueDiff:
                return True
            
            if index >= indexDiff:
                del store[nums[index-indexDiff] // (valueDiff + 1)]
            
            store[m] = val
            
        return False