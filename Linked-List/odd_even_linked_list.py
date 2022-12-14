"odd even linked list"
from list_node import ListNode
from linked_list import LinkedList

def odd_even_linked_list(head:ListNode) -> ListNode:
    "odd even linked list"
    if head is None or head.next is None:
        return head

    odd_node = head
    even_node = head.next
    even_head = even_node

    while even_node is not None and even_node.next is not None:
        odd_node.next = even_node.next
        even_node.next = even_node.next.next
        odd_node = odd_node.next
        even_node = even_node.next

    odd_node.next = even_head
    return head

def odd_even_linked_list2(self, head):
        """another linear solution """
        if head is None:
            return head;
        
        even = ListNode()
        odd = ListNode()
        odd_head = odd
        even_head = even
        is_odd = True
        
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            is_odd = not is_odd
            head = head.next
        even.next = None   
        odd.next = even_head.next
        return odd_head.next

if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.add_from_list([1,2,3,4,5])
    node = odd_even_linked_list(linkedlist.head)
    returnList = list()
    while node is not None:
        returnList.append(node.val)
        node = node.next
    print(returnList)
