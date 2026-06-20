# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Brute Force sol-changing node values
        # TC=O(2N)    SC=O(N)
        
        """curr=head
        stack=[]
        while curr!=None:
            stack.append(curr.val)
            curr=curr.next
            
        curr=head
        while curr!=None:
            e=stack.pop()
            curr.val=e
            curr=curr.next
        return head"""

        # Optimal sol-changing links
        # TC=O(N)  SC=O(1)

        curr=head
        prev=None
        while curr!=None:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev




        