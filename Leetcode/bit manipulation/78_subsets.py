# TC=O(N * 2**N) SC=O(N * 2**N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        total_subsets=1<<n
        for num in range(total_subsets):
            lst=[]
            for i in range(n):
                if num&(1<<i)!=0:
                    lst.append(nums[i])
            result.append(lst)
        return result