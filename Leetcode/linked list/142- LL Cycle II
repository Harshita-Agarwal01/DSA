# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Brute Force sol
        # TC=O(N)  SC=O(N)
        """curr=head
        my_set=set()
        while curr!=None:
            if curr in my_set:
                return curr
            else:
                my_set.add(curr)
            curr=curr.next
        return None"""

        # Optimal sol
        # TC=O(N)  SC=O(1)
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    fast=fast.next
                    slow=slow.next
                return slow
        return None

        
        

        
        