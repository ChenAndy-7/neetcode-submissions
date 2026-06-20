# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = list1, list2
        dummy = ListNode()
        tail = dummy

        while n1 and n2:
            if n1.val < n2.val:
                tail.next = n1
                n1 = n1.next
                
            else:
                tail.next = n2
                n2 = n2.next
            tail = tail.next
            
        if n1:
            tail.next = n1
        elif n2:
            tail.next = n2

        return dummy.next


