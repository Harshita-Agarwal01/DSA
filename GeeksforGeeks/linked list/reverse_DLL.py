"""
Structure of doubly linked list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
       
        # Brute Force sol
        # TC=O(2N)  SC=O(N)
        """curr=head
        lst=[]
        while curr!=None:
            lst.append(curr.data)
            curr=curr.next
        curr=head
        
        while curr!=None:
            e=lst.pop()
            curr.data=e
            curr=curr.next
            
        return head"""
        
        # Optimal sol
        # TC=O(N)   SC=O(1)
        if head.next is None:
            return head
        curr=head
        prev=None
        while curr!=None:
            front=curr.next
            curr.prev=front
            curr.next=prev
            prev=curr
            curr=front
        return prev