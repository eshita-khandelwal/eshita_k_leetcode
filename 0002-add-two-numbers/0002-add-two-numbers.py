# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversell(self,head):
        prev=None
        front=None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head1 = self.reversell(l1)
        # head2 = self.reversell(l2)
        head1=l1
        head2=l2
        sum1,carry=0,0
        head3 = ListNode()
        head3=None
        while head1 and head2:
            sum1 = head1.val + head2.val + carry
            carry = sum1//10
            sum2=0
            if sum1<=9:
                sum2=sum1
                carry=0
            else:
                sum2=sum1%10
            if head3==None:
                temp = ListNode()
                temp.val = sum2
                head3=temp
            else:
                t=head3
                temp=ListNode()
                temp.val = sum2
                while t.next:
                    t=t.next
                t.next=temp
            head1=head1.next
            head2=head2.next
        
        while head1:
            t=head3
            temp=ListNode()
            sum1 = head1.val+carry
            carry = sum1//10
            sum2=0
            if sum1<=9:
                sum2=sum1
                carry=0
            else:
                sum2=sum1%10
            temp.val = sum2
            while t.next:
                t=t.next
            t.next=temp
            head1=head1.next
        while head2:
            t=head3
            temp=ListNode()
            sum1 = head2.val+carry
            carry = sum1//10
            sum2=0
            if sum1<=9:
                sum2=sum1
                carry=0
            else:
                sum2=sum1%10
            temp.val = sum2
            while t.next:
                t=t.next
            t.next=temp
            head2=head2.next
        if carry>0:
            temp=ListNode()
            t=head3
            temp.val=carry
            while t.next:
                t=t.next
            t.next=temp
        return head3

            
            