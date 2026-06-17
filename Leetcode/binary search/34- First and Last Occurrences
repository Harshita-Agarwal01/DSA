
# Brute Force sol
# TC=O(N)   SC=O(1)
"""def searchRange(nums, target):
first=-1
last=-1
n=len(nums)
for i in range(n):
if nums[i]==target:
if first==-1:
first=i
last=i

return [first,last]
nums=[1,2,3,3,3,3,5,6]
target=3
print(searchRange(nums,target))"""

# Optimal sol- using upper and lower bound
# TC=O(logN)     SC=O(1)
class Solution(object):
    def lowerBound(self,nums,target):
        n=len(nums)
        first=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                first=mid
                high=mid-1
            else:
                low=mid+1
        return first
    
    def upperBound(self,nums,target):
        n=len(nums)
        last=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                last=mid
                high=mid-1
            else:
                low=mid+1

        return last
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        first=self.lowerBound(nums,target)
        last=self.upperBound(nums,target)
        if first==last:
            return [-1,-1]
        return [first,last-1]




