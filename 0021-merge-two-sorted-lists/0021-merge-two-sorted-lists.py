# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        head3=ListNode()
        head3=None
        while head1 and head2:
            value=0
            if head1.val>head2.val:
                value = head2.val
                head2=head2.next
            else:
                value = head1.val
                head1=head1.next

            n=ListNode()
            if head3==None:
                n.val=value
                head3=n
            else:
                temp=head3
                while temp.next:
                    temp=temp.next
                temp.next=n
                n.val=value

        while head1:
            temp = head3
            n=ListNode()
            if head3==None:
                n.val=head1.val
                head3=n
            else:
                temp=head3
                while temp.next:
                    temp=temp.next
                temp.next=n
                n.val=head1.val
            head1=head1.next

        while head2:
            temp = head3
            n=ListNode()
            if head3==None:
                n.val=head2.val
                head3=n
            else:
                temp=head3
                while temp.next:
                    temp=temp.next
                temp.next=n
                n.val=head2.val
            head2=head2.next

        return head3
        

        