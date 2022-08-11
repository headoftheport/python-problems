# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return root
        
        leftSide = self.flatten(root.left)
        rightSide = self.flatten(root.right)
        
        if leftSide is None:
            return root
        
        root.left = None
        
        curr = leftSide
        
        while curr.right is not None:
            curr = curr.right
            
        curr.right = rightSide
        root.right = leftSide
        return root