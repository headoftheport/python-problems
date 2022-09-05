"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value."""
class Solution:
    """solution"""
    def search_range(self, nums, target):
        """solution using recurssion"""
        return self.search_helper(nums, 0, len(nums)-1, target)
        
        
    def search_helper(self, nums, start, end, target):
        """recursive"""
        if start > end:
            return [-1, -1]
        
        mid = (start + end) // 2
        
        if nums[mid] < target:
            return self.search_helper(nums, mid + 1, end, target)
        
        if nums[mid] > target:
            return self.search_helper(nums, start, mid-1, target)
        
        nodes = [mid, mid]
        
        temp_left = self.search_helper(nums, start, mid-1, target)
        temp_right = self.search_helper(nums, mid+1, end, target)
        
        if start <= temp_left[0] < mid:
            nodes[0] = temp_left[0]
            
        if end >= temp_right[1] > mid:
            nodes[1] = temp_right[1]
        
        return nodes


    def search_range2(self, nums, target):
        """iterative"""
        left, right = -1, -1
        start , end = 0 ,len(nums)-1


        while start <= end:

            mid = ( start + end ) // 2
            if nums[mid] == target:
                left = mid
                end = mid-1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if left == -1:
            return [-1, -1]

        start = left
        end = len(nums) - 1

        while start <= end:

            mid = ( start + end ) // 2
            if nums[mid] == target:
                right = mid
                start = mid+1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return [start, right]

    def search_range3(self, nums, target):
        """recursive"""
        def search(low, high):

            if nums[low] == target == nums[high]:
                return [low, high]

            elif nums[low] <= target <= nums[high]:
                mid = (high + low) // 2
                l,r  = search(low, mid), search(mid+1, high)
                return max(l,r) if -1 in l+r else [l[0], r[1]]

            return [-1,-1]

        if len(nums) == 0:
            return [-1,-1]

        return search(0, len(nums)-1)


if __name__ == '__main__':
    print(Solution().search_range3([5,7,7,8,8,10], 8))




            
            
            
        
        
        
        