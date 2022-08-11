"""symmetric tree"""
from binary_tree_node import TreeNode

class Solution:
    """solution"""
    def is_symmetric(self, root:TreeNode) -> bool:
        """is symmetric"""
        if(not root): 
            return True
        
        temp_list = list()
        temp_list.append(root.left)
        temp_list.append(root.right)
        while len(temp_list) > 0:
            left_node = temp_list.pop()
            right_node = temp_list.pop()
            if not left_node and not right_node: 
                continue
                
            if not left_node or not right_node:
                return False
            
            if left_node.val != right_node.val:
                return False
            
            temp_list.append(left_node.left)
            temp_list.append(right_node.right)
            temp_list.append(left_node.right)
            temp_list.append(right_node.left)
            
        return True


    def is_symmetric_recursive(self, root) -> bool:
        """is symmetric recursive """
        if root is None:
            return True
        
        return self.helper(root.left, root.right)
    
    def helper(self, left_node, right_node):
        """helper method"""
        if left_node is None and right_node is None:
            return True
        
        if left_node is None or right_node is None:
            return False
        
        if left_node.val != right_node.val:
            return False
        
        return self.helper(left_node.left, right_node.right) and self.helper(left_node.right, right_node.left)