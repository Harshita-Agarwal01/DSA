class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Brute Force solution
        # TC=O(N**2)  SC=O(1)
        """n=len(nums)
        maxsum=float("-inf")
        if n==1:
            return nums[0]
        for i in range(n):
            total=0
            total+=nums[i]
            for j in range(i+1,n):
                total+=nums[j]
                if total>maxsum:
                    maxsum=total
        return maxsum"""

        # Kadane's Algorithm
        # Optimal solution
        # TC=O(N)  SC=O(1)
        n=len(nums)
        total=0
        maxsum=float("-inf")
        for i in range(n):
            total+=nums[i]
            if total>maxsum:
                maxsum=total
            if total<0:
                total=0
        return maxsum