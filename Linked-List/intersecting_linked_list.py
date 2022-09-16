"""intersecting linked list"""
class Solution:
    """solution"""
    def intersecting_linked_list(self, headA, headB):
        """
        without counting the nodes
        time complexity: O(m+n)
        space complexity: O(1)
        """

        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA != None else headB
            nodeB = nodeB.next if nodeB != None else headB
        
        return nodeA


    def intersecting_linked_list2(self, headA, headB):
        """
        without counting the nodes
        time complexity: O(m+n)
        space complexity: O(1)
        """

        def length(head):
            """to find the length of the linked list"""
            size = 0
            while head is not None:
                head = head.next
                size += 1
            return size

        sizeA = length(headA)
        sizeB = length(headB)

        while sizeA > sizeB:
            headA = headA.next
            sizeA -= 1

        while sizeB > sizeA:
            headB = headB.next
            sizeB -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def intersecting_linked_list3(self, headA, headB):
        """using set"""
        store = set()

        while headA:
            store.add(headA)
            headA = headA.next

        while headB:
            if headB in store:
                break
            headB = headB.next

        return headB

        
