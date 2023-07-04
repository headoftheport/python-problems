class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        """
        tc: O(n^2)
        sc: O(n^2)
        """
        sum_map = {}
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                total = nums1[i] + nums2[j]
                if total not in sum_map:
                    sum_map[total] = 0
                sum_map[total] += 1
                
        
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                total = nums3[i] + nums4[j]
                if -total in sum_map:
                    res += sum_map[-total]
                    
                    
        return res
        