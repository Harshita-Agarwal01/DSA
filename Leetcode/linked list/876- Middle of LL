# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Brute Force sol
        # TC=O(N+N/2)  SC=O(1)
        """curr=head
        c=1
        while curr.next is not None:
            curr=curr.next
            c+=1
        mid=c//2
        count=0
        curr=head
        while count<mid:
            curr=curr.next
            count+=1
        return curr"""

        # Optimal- Tortoise-Hare Approach
        # TC=O(N/2)   SC=O(1)
        fast=head
        slow=head
        
        while fast is not None and fast.next is not None:  
            fast=fast.next.next
            slow=slow.next
            
        return slow