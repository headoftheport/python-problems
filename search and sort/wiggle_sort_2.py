class Solution:

    def wiggle_sort(self, nums):
        
        copy = sorted(nums)
        n = len(nums)
        m = (n+1) >> 1

        i = m - 1
        j = 0
        while i >= 0:
            nums[j] = copy[i]
            i -= 1
            j += 2

        i = n - 1
        j = 1
        while i >= m:
            nums[j] = copy[i]
            i -= 1
            j += 2