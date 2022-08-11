"Remove Linked List Elements"

from list_node import ListNode
from linked_list import LinkedList

def remove_elements( head:ListNode, val: int) -> ListNode:
    "remove elements"
    if head is None:
        return None
    head.next = remove_elements(head.next, val)
    return head.next if head.val == val else head


def remove_elements_iterative(head:ListNode, val:int) -> ListNode:
    "remove elements"
    while head and head.val == val:
        head = head.next

    if not head:
        return None

    prev = head
    curr = head.next

    while curr:
        if curr.val is val:
            prev.next = curr.next
            curr = curr.next
            continue

        prev = curr
        curr = curr.next

    return head

if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.add_from_list([1,2,6,3,4,5,6])
    node = remove_elements_iterative(linkedlist.head,6)
    returnList = list()
    while node is not None:
        returnList.append(node.val)
        node = node.next
    print(returnList)
