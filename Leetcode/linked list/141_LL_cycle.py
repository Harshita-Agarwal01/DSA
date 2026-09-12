# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Brute Force sol- Using set
        # TC=O(N)  SC=O(N)
        """temp=head
        my_set=set()
        while temp!=None:
            if temp in my_set:
                return True
            my_set.add(temp)    #adding node (temp) and not its value (temp.val) bcz duplicates are posssible
            temp=temp.next
        return False"""

        # Optimal sol- Tortoise-Hare Approach
        # TC=O(N)  SC=O(1)
        fast=head
        slow=head
        while fast !=None and fast.next != None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False

        