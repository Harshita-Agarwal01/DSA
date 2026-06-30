class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # we use XOR here as it works on different numbers
        # TC=O(32)  SC=O(1)
        """ans=start^goal
        count=0
        for i in range(32):
            if ans & (1<<i)!=0:   # to check for set bit
                count+=1
        return count"""

        # TC=O(logN)  SC=O(1)
        # more efficient as it iterates only over the set bits rather than all 32 bits
        ans=start^goal
        count=0
        while ans>0:
            ans=ans & (ans-1) # removes the rightmost set bit
            count+=1
        return count
