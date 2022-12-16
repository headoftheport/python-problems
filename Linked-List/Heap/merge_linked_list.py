"""merge n linked list"""
from queue import PriorityQueue
import list_node
class Solution:
    """using priority queue"""
    def merge(lists):
        """
        time O(NlogK)
        space: O(k)
        """
        dummy = list_node()
        curr = dummy
        que = PriorityQueue()
        for node in lists:
            if node:
                que.put((node.val, node))

        
        while que.qsize() > 0:
            curr.next = que.get()[1]
            curr = curr.next
            if curr.next: 
                que.put((curr.next.val, curr.next))

        return dummy.next
