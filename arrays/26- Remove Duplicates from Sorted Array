class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1    