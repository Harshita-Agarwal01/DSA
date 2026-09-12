class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TC=O(N)  SC=O(1)
        """n=len(nums)
        return (n*(n+1))//2 - sum(nums)""" 

        n=len(nums)
        actual_sum,req_sum=0,0
        for i in range(n):
            actual_sum+=nums[i]
        for i in range(n+1):
            req_sum+=i
        return req_sum-actual_sum