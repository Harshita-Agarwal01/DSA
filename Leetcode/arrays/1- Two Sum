class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #TC=O(N)  SC=O(N)
        n=len(nums)
        freq={}
        for i in range(n):
            find=target-nums[i]
            if find in freq:
                return [freq[find],i]
            else:
                freq[nums[i]]=i
            
            