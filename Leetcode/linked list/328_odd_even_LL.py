# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Brute Force sol
        # TC=O(N/2 + N/2 + N = 2N)  SC=O(N)
        """if head is None or head.next is None:
            return head
        lst=[]
        curr=head
        while curr!=None and curr.next!=None:
            lst.append(curr.val)
            curr=curr.next.next
        if curr!=None:
            lst.append(curr.val)
        curr=head.next
        while curr!=None and curr.next!=None:
            lst.append(curr.val)
            curr=curr.next.next
        if curr!=None:
            lst.append(curr.val)
        curr=head
        index=0
        while curr:
            curr.val=lst[index]
            curr=curr.next
            index+=1
        
        return head"""

        # Optimal sol
        # TC=O(N/2)  SC=O(1)
        if head is None or head.next is None:
            return head
        odd=head
        even=head.next
        even_head=even
        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return head
        

        