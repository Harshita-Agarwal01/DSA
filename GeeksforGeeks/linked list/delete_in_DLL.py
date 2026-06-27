"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        # code here
        
        if x==1:
            temp=head
            head=head.next
            if head:
                head.prev=None
            del temp
            return head
        curr=head
        c=0
        while curr and c<x-2:
            curr=curr.next
            c+=1
        temp=curr.next
        curr.next=temp.next
        if temp.next:
            temp.next.prev=curr
        del temp
        return head