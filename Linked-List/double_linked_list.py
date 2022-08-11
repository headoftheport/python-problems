"double linked list"

from double_list_node import Node

class DoubleLinkedList(object):
    """init"""
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def get( self,index):
        """get"""
        if index >= self.length:
            return - 1

        counter = 0
        itr = self.head
        while counter < index:
            itr = itr.nex
            counter += 1

        return itr.val

    def add_at_head(self, val):
        """add at head"""
        node = Node(val)
        if self.head is None:
            self.head = node
            self.length += 1
            return

        node.nex = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
        return

    def add_at_tail(self, val):
        





