from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        # Brute Force sol
        # TC=O(N**2)  SC=O(1)
        """temp1=head
        result=[]
        while temp1!=None:
            temp2=temp1.next
            while temp2!=None:
                if temp1.data+temp2.data==target:
                    result.append([temp1.data,temp2.data])
                temp2=temp2.next
            temp1=temp1.next
        return result"""
        
        # Better sol
        # TC=O(N)  SC=O(N)
        """curr=head
        result=[]
        my_set=set()
        while curr!=None:
            find=target-curr.data
            if find in my_set:
                result.append([find,curr.data])
            else:
                my_set.add(curr.data)
            curr=curr.next
        
        return sorted(result)"""
        
        # Optimal sol
        # TC=O(2N)  SC=O(1)
        left=head
        right=head
        result=[]
        while right.next!=None:
            right=right.next
        while left.data<right.data and left!=None and right!=None:
            if left.data+right.data>target:
                right=right.prev
            elif left.data+right.data<target:
                left=left.next
            else:
                result.append([left.data,right.data])
                left=left.next
                right=right.prev
        return result