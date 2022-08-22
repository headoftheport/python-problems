"""3 sum"""
from itertools import permutations

class Solution:
    """solution"""
    def three_sum(self, nums):
        """sorts the array to solve the problem"""
        #time complexity: o(n^2) + additional effort to sort the array
        storage = []
        nums = sorted(nums)
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            ans = self.two_sum(nums[index+1:], 0 - value)
            for i in ans:
                storage.append(i + [value])
            
        return storage
        
        
        
    def two_sum(self, nums, target):
        """two sum"""
        i = 0
        j = len(nums) - 1
        ans = []
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
                continue
            elif nums[i] + nums[j] < target:
                i += 1
                continue
            ans.append([nums[i], nums[j]])
            i += 1
            j -= 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i = i + 1
            while j >= 0 and nums[j] == nums[j+1]:
                j = j - 1
                
        return ans

    def three_sum2(self, nums):
        """some different way to solve"""

        pos , neg = [], []
        zeros = 0
        ans = set()
        for i in nums:
            if i == 0:
                zeros += 1
            elif i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
        N = set(neg)
        P = set(pos)
        print(N, P)
        if zeros > 0:

            if zeros > 2:
                ans.add(tuple([0,0,0]))
            
            for value in N:
                target = -1*value
                if target in P:
                    ans.add(tuple(sorted([target, 0 , value])))

        
        for x, y in permutations(pos, 2):
            target = -1*(x + y)
            if target in N:
                ans.add(tuple(sorted([target, x , y])))


        for x, y in permutations(neg, 2):
            target = -1*(x + y)
            if target in P:
                ans.add(tuple(sorted([target, x , y])))

        return ans
        




    
                