"""jump game"""

class Solution:
    """solution"""
    def jump_game(self,nums):
        """iterative solution"""
        goal = len(nums)-1
        
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0
