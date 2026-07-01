class Solution:
    # TC=O(N* 2**N)  SC=O(N)
    def powerset(self,ind,subset,nums):
        if ind>=len(nums):
            self.result.append(subset.copy())
            return
        subset.append(nums[ind])
        self.powerset(ind+1,subset,nums)
        subset.pop()
        self.powerset(ind+1,subset,nums)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result=[]
        subset=[]
        ind=0
        self.powerset(ind,subset,nums)
        return self.result