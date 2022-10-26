"""solution"""
class Solution:
    """solution"""
    def find_peak(self, nums):
        """
        time: O(logn)
        space: O(1)
        """

        start = 0
        end = len(nums)-1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1

        return start