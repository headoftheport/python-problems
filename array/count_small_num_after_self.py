from ast import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        divid and conquer
        tc: nlogn
        sc: n
        """
        def sort(enums):
            half = len(enums) // 2
            if half:
                left, right = sort(enums[:half]), sort(enums[half:])
                for i in range(len(enums))[::-1]:
                    
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    else:
                        enums[i] = right.pop()
                        
            return enums
        
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller