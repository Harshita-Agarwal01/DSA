class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Force sol
        # TC=O(N)+ O((N/2)+1) ~ O(N) SC=O(N/2 + 1)
        """if len(nums)==1:
            return nums[0]
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        for key,val in hash_map.items():
            if val==1:
                return key"""

        # Optimal sol
        # TC=O(N)  SC=O(1)
        ans=0
        for num in nums:
            ans=ans^num
        return ans


        