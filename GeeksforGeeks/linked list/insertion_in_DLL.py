
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None



class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        new_node=Node(x)
        
        curr=head
        count=0
        while curr and count < p:
            curr=curr.next
            count+=1
        if curr is None:
            return head
        new_node.next=curr.next
        new_node.prev=curr
        if curr.next:
            curr.next.prev=new_node
        curr.next=new_node
        return head