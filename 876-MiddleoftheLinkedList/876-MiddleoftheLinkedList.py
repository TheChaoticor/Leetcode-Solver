# Last updated: 3/25/2025, 8:55:36 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next==None:
            return head

        c=0
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        acm=l//2
        lk=0
        curr=head
        for _ in range(acm):
            curr = curr.next
            
        return curr 
                
            
        



