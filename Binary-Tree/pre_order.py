from inspect import stack
from binary_tree_node import TreeNode


class Solution:
    "solution"
    def pre_order_traversal(self, node:TreeNode) -> list:
        """recursive"""
        ans = []
        def dfs(node:TreeNode):
            if node is None:
                return

            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        return dfs(node)


    def pre_order_traversal_iterative(self, node:TreeNode) -> list:
        """iterative"""
        if node is None:
            return []
        return_list = []
        local_stack = [node]
        while local_stack:
            temp = local_stack.pop()
            if temp:
                return_list.append(temp.val)
                local_stack.append(temp.right)
                local_stack.append(temp.left)

        return return_list


if __name__ == "__main__":

    
