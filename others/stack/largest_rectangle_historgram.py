class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        tc: n
        sc: n
        """
        heights.append(0)
        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            
            while heights[stack[-1]] > heights[i]:
                
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
    
            stack.append(i)
            
        return maxArea