
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

    
    def connect3(self, root):
        """iterative without dummy node"""
        node = root
        
        while node and node.left:
            temp = node
            start = temp.left
            while temp:
                
                if start == temp.left:
                    start.next = temp.right
                    start = start.next
                elif start == temp.right:
                    temp = temp.next
                else:
                    start.next = temp.left
                    start = start.next
                    
            node = node.left
            
        return root


    def connect4(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """recursive solution"""
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
            
        return root

    def connect5(self, root):
        """iterative"""
        curr = root
        while curr and curr.left:
            temp = curr
            while temp:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next   
            curr = curr.left
            
        return root
    
    

                    
                
            
            
    
        
        