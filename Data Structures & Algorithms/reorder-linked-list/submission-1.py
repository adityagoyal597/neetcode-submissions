# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        # beginning of the second half
        second=slow.next
        # splitting the list into two half
        slow.next=None

        # reversing the second list
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        # after loop, second points to none
        #prev points to the first element in the second reversed list
         
        second =prev
        first=head

        # as the second half can be shorter than first half the odd case
        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
