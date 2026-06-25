# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Brute Force sol- Two pass
        # TC=O(2N)  SC=O(1)
        """if head == None or head.next==None:
            
            return 
        curr=head
        count=1
        while curr.next!=None:
            curr=curr.next
            count+=1
        if count==n:
            new_head=head.next
            del head
            return new_head
        k=count-n
        curr=head
        for i in range(k-1):
            curr=curr.next
        curr.next=curr.next.next
        return head"""

        # Optimal sol- One pass
        # TC=O(N)  SC=O(1)
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        if fast==None:
            return head.next
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head