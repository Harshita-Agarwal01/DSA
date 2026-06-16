# Brute Force sol
# TC=O(n)   SC=O(1)
"""def searchInsert(nums, target):
    n=len(nums)
    for i in range(n):
        if nums[i]>=target:
            return i
    return n
nums=[1,2,3]
target=1
print(searchInsert(nums,target))"""

# Optimal sol- Lower bound
# TC=O(logN)  SC=O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        lb=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
