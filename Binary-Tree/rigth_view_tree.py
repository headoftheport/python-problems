"""the right view of binary tree"""
from collections import deque
class Solution:
    """solution"""
    def right_view(self, root):
        """
        using DFS
        time: O(n)
        space: O(n)
        """
        ans = list()
        def dfs(node, ans, level):
            """dfs"""
            if node is None:
                return
            
            if len(ans) <= level:
                ans.append(node.val)

            dfs(node.right, ans, level+1)
            dfs(node.left, ans, level+1)

        dfs(root, ans, 0)
        return ans


    def right_view_2(self, root):
        """
        using BFS
        time: O(n)
        space: O(n)
        """
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    ans.append(node.val)
                if node.right: 
                    queue.append(node.right)
                if node.left:
                     queue.append(node.left)
        return ans
