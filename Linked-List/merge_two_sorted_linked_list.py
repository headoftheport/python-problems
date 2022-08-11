"""merge two sorted linked list"""
from list_node import ListNode
from linked_list import LinkedList


def merge_two_linked_list(list1:ListNode, list2:ListNode):
    """merge two linked list"""
    if list1 is None:
        return list2

    if list2 is None:
        return list1


    dummy = ListNode()
    if list1.val < list2.val:
        dummy.next = list1
        list1.next = merge_two_linked_list(list1.next, list2)
    else:
        dummy.next = list2
        list2.next = merge_two_linked_list(list1, list2.next)

    return dummy.next


if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.add_from_list([1,2,3,4,5])
    linkedlist2 = LinkedList()
    linkedlist2.add_from_list([1,2,3,4,5])

    node = merge_two_linked_list(linkedlist.head, linkedlist2.head)
    returnList = list()
    while node is not None:
        returnList.append(node.val)
        node = node.next
    print(returnList)




