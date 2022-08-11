"""in-order traversal"""
from binary_tree_node import TreeNode

class Solution:
    """solution"""
    def inorder_recursive(self, root:TreeNode) -> list:
        """recursive"""
        inorder_list = list()

        def helper(root:TreeNode, inorder_list:list) -> list:

            if root is None:
                return inorder_list

            helper(root.left, inorder_list)
            inorder_list.append(root.val)
            helper(root.right, inorder_list)
            return inorder_list

        return helper(root, inorder_list)


    def inorder_iterative(self, root:TreeNode) -> list:
        """iterative solution"""
        inorder_list = list()
        stack = list()

        if root is None:
            return inorder_list

        node = root

        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            inorder_list.append(node.val)
            node = node.right

        return inorder_list


    def inorder_morris(self, root:TreeNode) -> list:
        """morris traversal"""

        if root is None:
            return []
        inorder_list = list()
        node = root
        pre = None


        while node:
            if node.left is None:
                inorder_list.append(node.val)
                node = node.right
            else:
                pre = node
                node = node.left
                while node.right is not None:
                    node = node.right

                node.right = pre
                temp = pre.left
                pre.left = None
                node = temp

        return inorder_list

        

