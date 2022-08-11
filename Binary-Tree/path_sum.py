"""path sum"""
from binary_tree_node import TreeNode

class Soultion:
    """soultion"""
    def has_path_sum(self, root: TreeNode, target_sum: int) -> bool:
        """has path sum"""
        if root is None:
            return False
        
        if root.left is None and root.right is None and target_sum - root.val == 0:
            return True
        
        
        return self.has_path_sum(root.left, target_sum - root.val) or self.has_path_sum(root.right, target_sum - root.val)


    def has_path_sum_dfs(self, root: TreeNode, target_sum: int) -> bool:
        """has path sum DFS solution using stack"""
        if root is None:
            return False
        
        stack = []
        stack.append((root, root.val))
        
        while len(stack) > 0:
            node, val = stack.pop()
            if node.left is None and node.right is None and val == target_sum:
                return True
            
            if node.left is not None:
                stack.append((node.left, val + node.left.val))
            
            if node.right is not None:
                stack.append((node.right, val + node.right.val))
   
        return False


    def has_path_sum_bfs(self, root: TreeNode, target_sum: int) -> bool:
        """has path sum bfs using queue"""
        if root is None:
            return False
        
        queue = []
        queue.append((root, target_sum - root.val))
        
        while len(queue) > 0:
            node, val = queue.pop(0)
            if node.left is None and node.right is None and val == 0:
                return True
            
            if node.left is not None:
                queue.append((node.left, val - node.left.val))
            
            if node.right is not None:
                queue.append((node.right, val - node.right.val))
                
            
        return False


    def has_path_sum_inorder(self, root: TreeNode, targetSum: int) -> bool:
        """has path sum inorder"""
        if root is None:
            return False
        
        stack = []
        curr = root
        sumValue = 0
        pre = None
        while curr or len(stack) > 0:
            while curr:
                sumValue = sumValue + curr.val
                stack.append(curr)
                curr = curr.left
                
            curr = stack[-1]
            if curr.left is None and curr.right is None and sumValue == targetSum:
                return True
            
            if curr.right and pre != curr.right:
                curr = curr.right
            else:
                sumValue = sumValue - curr.val
                pre = curr
                curr = None
                stack.pop()
                
        return False