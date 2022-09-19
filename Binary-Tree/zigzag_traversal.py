"""solution"""
from collections import deque

class Solution:
    """solution"""
    def zigzag_traversal(self, root):
        """
        using DFS
        O(n)
        O(logn)
        """
        store = []
        q = deque()
        if root is None:
            return store

        q.append(root)
        zig = False
        while q:
            size = len(q)
            temp = []
            while size > 0:
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
                if not zig:
                    temp.append(node.val)
                else:
                    temp.insert(0, node.val)
                size = size - 1

            zig = not zig
            store.append(temp)

        return store


    def zigzag_traversal2(self, root):
        """
        DFS
        O(n)
        O(logn)
        """
        store = []
        self.zigzag(root, store, 0)
        return store

    def zigzag(self, root, res, level):
        """
        recursive
        """
        if root is None:
            return

        if len(res) <= level:
            res.append([])

        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)

        self.zigzag(root.left, res, level+1)
        self.zigzag(root.right, res, level+1)
        return
