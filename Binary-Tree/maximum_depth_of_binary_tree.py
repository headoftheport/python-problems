"""maximum depth of binary tree"""
from binary_tree_node import TreeNode


class Solution:
    """solution"""
    def max_depth(self, root) -> int:
        """max depth"""
        if root is None:
            return 0
        
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


    def max_depth_dfs(self, root) -> int:
        """dfs solution"""
        if root is None:
            return 0
        
        stack = []
        value_stack = []
        
        stack.append(root)
        value_stack.append(1)
        depth = 0
        
        while len(stack) > 0:
            curr = stack.pop()
            curr_val = value_stack.pop()
            depth = max(curr_val, depth)
            
            if curr.left is not None:
                stack.append(curr.left)
                value_stack.append(curr_val + 1)
                
            if curr.right is not None:
                stack.append(curr.right)
                value_stack.append(curr_val + 1)
                
        return depth


    def max_depth_bfs(self, root) -> int:
        """max depth bfs"""
        if root is None:
            return 0
        
        stack = []
        value_stack = []
        
        stack.append(root)
        value_stack.append(1)
        depth = 0
        
        while len(stack) > 0:
            size = len(stack)
            while size > 0:
                node = stack.pop(0)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                size = size - 1
                    
            depth = depth + 1
                
        return depth

        