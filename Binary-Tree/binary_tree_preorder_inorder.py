"""binary tree from pre-order and in-order"""
from binary_tree_node import TreeNode

class Solution:
    """solution"""
    def build_tree(self, preorder, inorder) -> TreeNode:
        """build tree"""
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.build_tree(preorder[1:mid+1], inorder[:mid])
        root.right = self.build_tree(preorder[mid+1:], inorder[mid+1:])
        return root


    def build_tree_iterative(self, preorder, inorder):
        """iterative solution"""
        if len(preorder) == 0:
            return None
        
        
        root = TreeNode(preorder[0])
        curr = root
        
        i = 1
        j = 0
        
        stack = []
        
        while i < len(preorder):
            print(i, j)
            if curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i])
                stack.append(curr)
                curr = curr.left
                i = i + 1
            else:
                j = j + 1
                while len(stack) > 0 and stack[-1].val == inorder[j]:
                    curr = stack.pop()
                    j =  j + 1
                curr.right = TreeNode(preorder[i])
                i = i + 1
                curr = curr.right
                
        return root