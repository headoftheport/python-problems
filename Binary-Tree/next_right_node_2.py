
# Definition for a Node.
class Node:
    """node"""
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """solution"""
    def connect(self, root: 'Node') -> 'Node':
        """recursive"""
        levels = []
        
        def helper(node, level ):
            print(levels)
            if node is None:
                return 
            
            if len(levels) < level:
                levels.append(node)
            else:
                levels[level-1].next = node
                levels[level-1] = node
                
            helper(node.left, level + 1)
            helper(node.right, level + 1)
            
        helper(root, 1)
        return root

    def connect_iterative(self, root: 'Node') -> 'Node':
        """iterative solution"""
        node = root
        
        while node:
            dummy = Node(0)
            curr = dummy
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                    
                node = node.next
                
            node = dummy.next
            dummy.next = None
            
        return root
    
    

                    
                
            
            
    
        
        