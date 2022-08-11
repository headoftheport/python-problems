"""linked list implementation"""
from list_node import ListNode

class LinkedList:
    """linked list implementation"""
    def __init__(self) -> None:
        self.head = None

    def add_from_list(self, nums):
        """this method creates linked list from array of numbers"""
        self.head = ListNode()
        temp = self.head
        for i in nums:
            node = ListNode(i)
            temp.next = node
            temp = temp.next

        self.head = self.head.next
#to be added
        