# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = -float('inf')
    
        def helper(root):
            nonlocal maxSum
            
            if root == None:
                return 0
            
            leftValue = max(helper(root.left),0)
            rightValue = max(helper(root.right),0)
            
            # maxLeftChild = leftValue[0] if leftValue[2] < leftValue[0] else leftValue[2]
            # maxRightChild = rightValue[0] if rightValue[2] < rightValue[0] else rightValue[2]
            
            maxSum = max(maxSum, leftValue + root.val + rightValue)

            return max(leftValue + root.val, rightValue + root.val)
        
        helper(root)
        return maxSum
        