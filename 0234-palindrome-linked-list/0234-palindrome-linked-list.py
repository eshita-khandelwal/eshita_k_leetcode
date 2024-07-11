# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        cur,prev=slow,None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp


        t=head

        while head and prev:
            if t.val!=prev.val:
                return False
            t=t.next
            prev=prev.next
        
        return True
        