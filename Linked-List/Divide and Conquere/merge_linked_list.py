# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import list_node

class Solution:
    def mergeKLists(self, lists):
        """
        tc: O(nlogk)
        sc: O(1)
        """
        return self.divide_and_merge(lists, 0, len(lists)-1)
    
    
    def divide_and_merge(self, lists, start, end):
        
        if start == end:
            return lists[start]
        
        if end - start == 1:
            return self.merge(lists[start], lists[end])
        
        
        left = self.divide_and_merge(lists, start, (start+end) // 2)
        right = self.divide_and_merge(lists, ((start+end) // 2) + 1, end)
        
        return self.merge(left, right)
    
    def merge(self,list1, list2):
        
        dummy = list_node()
        curr = dummy
        
        while list1 != None or list2 != None:
            
            if list1 == None:
                curr.next = list2
                list2 = list2.next
                
            elif list2 == None:
                curr.next = list1
                list1 = list1.next
                
            elif list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                
            else:
                curr.next = list2
                list2 = list2.next
                    
            curr = curr.next
            
        return dummy.next
            