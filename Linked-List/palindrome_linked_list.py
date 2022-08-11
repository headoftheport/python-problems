"palindrome linked list"
from list_node import ListNode
from linked_list import LinkedList

def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
       
        firstHalf = self.findTheMid(head)
        NextHalfStart = self.reverseList(firstHalf.next)
        
        start = head
        sec_Position = NextHalfStart
        result = True
        while sec_Position != None and result:
            if start.val != sec_Position.val:
                result = False
                
            start = start.next
            sec_Position = sec_Position.next
            
            
        firstHalf.next = self.reverseList(NextHalfStart)
        return result
    
    
    def findTheMid(self, head):
        
        fastPointer = head
        slowPointer = head
        
        while (fastPointer.next != None and fastPointer.next.next != None):
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        
        return slowPointer
    
    
    
    def reverseList(self, head):
        
        prev = None
        curr = head
        
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev