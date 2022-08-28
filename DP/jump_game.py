"""jump game"""

class Solution:
    """solution"""
    def jump_game(self,nums):
        """backward iterative solution"""
        goal = len(nums)-1
        
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0


    def jump_game2(self, nums):
        """forward interation"""
        m = 0
        for index, value in enumerate(nums):
            
            if index > m:
                return False
            
            m = max(m, index+value)
            
        return True


    def jump_game3(self, nums):
        """iterative solution"""
        
        if len(nums) == 1: 
            return True
        
        steps = nums[0]
        length = len(nums) - 1
        
        for index in range(1, len(nums)):
            print(steps, index, nums[index])
            if steps <= 0 and length != 0:
                return False
            
            if steps >= length:
                return True
            
            steps -= 1
            length -= 1
            steps = max(steps, nums[index])
            
        return False

    def jump_game4(self, nums):
        """iterative solution"""
        index = 1
        max_index = nums[0]

        while index < len(nums) and index <= max_index:
            max_index = max(max_index, index+ nums[index])
            if max_index >= len(nums) - 1:
                return True
            index += 1

        return max_index >= len(nums-1)




