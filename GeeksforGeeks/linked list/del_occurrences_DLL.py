"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        # TC=O(N)  SC=O(1)
        curr=head
        while curr!=None:
            front=curr.next
            
            if curr.data==x:
                prev=curr.prev
                if prev:
                    prev.next=front
                else:
                    head=front
                if front:
                    front.prev=prev
            curr=curr.next
        return head
                