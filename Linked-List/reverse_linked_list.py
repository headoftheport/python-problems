""" reverse linked list solutions"""

from linked_list import LinkedList
from list_node import ListNode


def reverse_list(head: ListNode) -> ListNode:
    """iterative"""
    if head is None or head.next is None:
        return head

    prev = None
    curr = head

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def reverse_list_recursive(head: ListNode) -> ListNode:
    """recursive solution"""
    if head is None or head.next is None:
        return head

    rest = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.add_from_list([1,2,3,4,5])
    node = reverse_list(linkedlist.head)
    returnList = list()
    while node is not None:
        returnList.append(node.val)
        node = node.next
    print(returnList)
#to be added
