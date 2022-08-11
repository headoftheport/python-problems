"""post order"""
from binary_tree_node import TreeNode

class Solution:
    """solution"""
    def post_order(self, root:TreeNode) -> list:
        """post order"""
        return_list = list()

        def helper(root, return_list):
            """helper"""
            if root is None:
                return return_list

            helper(root.left, return_list)
            helper(root.right, return_list)
            return_list.append(root.val)

            return return_list
        return helper(root, return_list)


    def post_order_iterative(self, root:TreeNode) -> list:
        """post order iterative"""
        int_list = list()
        stack = list()

        if root is None:
            return int_list

        stack.append(root)

        while len(stack) != 0:
            node = stack.pop()
            int_list.insert(0, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return int_list


    def post_order_traversal_iterative_2(self, root:TreeNode) -> list:
        """post order iterative solution 2"""
        int_list = list()
        stack = list()

        if root is None:
            return int_list

        stack.append(root)
        stack.append(root)

        while len(stack) != 0:
            node = stack.pop()

            if(len(stack) == 0 or stack[-1] == node):
                if node.left:
                    stack.append(node.left)
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)
                    stack.append(node.right)
            else:
                int_list.append(node.val)

        return int_list

            
        


