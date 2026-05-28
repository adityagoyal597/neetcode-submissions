# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        nodes=[]

        if cur==None:
            return None
            
        while (cur.next!=None):
            nodes.append(cur)
            cur=cur.next

        newHead=cur

        newCur=newHead

        while(nodes):
            newCur.next=nodes.pop()
            newCur=newCur.next
        
        newCur.next=None

        return newHead


        