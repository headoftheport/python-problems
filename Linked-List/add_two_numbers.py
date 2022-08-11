"""add two numbers"""

from linked_list import LinkedList
from list_node import ListNode

def add_two_numbers(list_node1:ListNode, list_node2: ListNode) -> ListNode:
    """add two numbers"""
    dummy = ListNode()
    list1,list2,curr = list_node1, list_node2, dummy
    carry = 0
    while list1 is not None or list2 is not None:

        val1 = 0 if list1 is None else list1.val
        val2 = 0 if list2 is None else list2.val

        total = carry + val1 + val2
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        if list1 is not None:
            list1 = list1.next

        if list2 is not None:
            list2 = list2.next


    if carry > 0:
        curr.next = ListNode(carry)

    return dummy.next

def add_two_numbers_recursive(list_node1:ListNode, list_node2: ListNode) -> ListNode:
    """add two numbers"""
    if list_node1 is None:
        return list_node2

    if list_node2 is None:
        return list_node1

    total = list_node1.val + list_node1.val
    if total < 10:
        node = ListNode(total)
        node.next = add_two_numbers_recursive(list_node1.next, list_node2.next)
        return node

    node = ListNode(total % 10)
    node.next = add_two_numbers_recursive(ListNode(total // 10), add_two_numbers_recursive(list_node1.next, list_node2.next))
    return node

if __name__ == '__main__':

    linkedlist1 = LinkedList()
    linkedlist1.add_from_list([1,2,3,4,5])
    linkedlist2 = LinkedList()
    linkedlist2.add_from_list([1,2,3,4,5])
    node = add_two_numbers_recursive(linkedlist1.head,linkedlist1.head)
    returnList = list()
    while node is not None:
        returnList.append(node.val)
        node = node.next
    print(returnList)
