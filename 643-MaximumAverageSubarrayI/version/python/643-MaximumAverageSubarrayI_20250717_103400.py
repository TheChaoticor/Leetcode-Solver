# Last updated: 7/17/2025, 10:34:00 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if fast==slow:
                return True
        return False        

             
        



        