'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
# TC=O(N)    SC=O(1)
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                count=1
                fast=fast.next
                while fast!=slow:
                    count+=1
                    fast=fast.next
                return count
        return 0