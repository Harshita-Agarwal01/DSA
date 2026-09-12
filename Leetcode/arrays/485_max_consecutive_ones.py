class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count,maxcount=0,0

        for i in range(n):
            if nums[i]==1:
                count+=1
            if count>maxcount:
                maxcount=count
            elif nums[i]==0:
                count=0
        return maxcount
        
        
        