"""generate all permutations"""
class Solution:
    """solution"""
    def permute(self, nums):
        """
        backtrack
        time: O(n*n!)
        space: O(n!)
        """
        ans = []

        def backtrack(nums, start):

            if start == len(nums):
                temp = []
                for item in nums:
                    temp.append(item)
                ans.append(temp)
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(nums, 0)
        return ans

    
    def permute2(self, nums):
        """
        iteration
        time: O(n*n!)
        space: O(n!)
        """
        ans = [[]]

        for n in nums:
            temp = []
            for item in ans:
                for i in range(len(item)+1):
                    temp.append(item[:i] + [n] + item[i:])
            ans = temp

        return temp



            