"""level order"""
from binary_tree_node import TreeNode

class Solution:
    """level order"""


    def level_order_iterative(self, root:TreeNode):
        """iterative solution"""
        node_queue = []
        return_list = []
    
        if root is None:
            return return_list
        
        node_queue.append(root)
        
        while len(node_queue) > 0:
            # level will be the number of newly added nodes
            level = len(node_queue)
            temp = []
            for i in range(level):
                node = node_queue.pop(0)
                temp.append(node.val)
                
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
                    
            return_list.append(temp)
            
        return return_list


    
    def level_order_recursive(self, root:TreeNode):
        """recursive solution"""
        return_list = []

        def helper(root, return_list, depth):
            """helper """
            if root is None:
                return return_list

            if depth >= len(return_list):
                return_list.append(list())

            return_list[depth].append(root.val)
            helper(root.left, return_list, depth+1)
            helper(root.right, return_list, depth+1)
            return return_list

        return helper(root, return_list, 0)


