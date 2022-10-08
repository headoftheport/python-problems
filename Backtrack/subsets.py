"""subsets"""
class Solution:
    """solution"""
    def subsets(self, nums):
        """
        backtrack
        time; O(n*2^n)
        space: O(n)
        """
        ans = []

        def backtrack(start, curr):
            """backtrack"""
            ans.append(curr)
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.remove(len(nums)-1)

            return

        backtrack(0, [])
        return ans