# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return root
        pLeft, pRight, qLeft, qRight = False, False, False, False
        
        if root == p:
            return p
            
        if root == q:
            return q
            
        
        pLeft = self.search(root.left, p)
        if not pLeft:
            pRight = True
            
        qLeft = self.search(root.left, q)
        if not qLeft:
            qRight = True
               
        if pLeft and qLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pRight and qRight:
            return self.lowestCommonAncestor(root.right, p, q)
            
        return root
        
        
        
    def search(self, root, p, pStore):
        
        if root is None:
            return None
        
        if root == p:
            return True
        
        return self.search(root.left, p) or self.search(root.right, p)

    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestorRecurse(self, root, p, q):
        """recursive"""
        def recurse(curr):
            
            if curr is None:
                return False
            
            
            left = recurse(curr.left)
            right = recurse(curr.right)
            
            mid = curr == p or curr == q
            
            if mid + left + right >= 2:
                self.ans = curr
                
            return mid or left or right
        
        
        recurse(root)
        return self.ans


    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        stack = [root]
        parent = {root:None}
        
        while p not in parent or q not in parent:
            
            node = stack.pop()
        
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
                
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
            
        
        ans = set()
        
        
        while p:
            ans.add(p)
            p = parent[p]
            
        while q not in ans:
            q = parent[q]
            
        return q
        