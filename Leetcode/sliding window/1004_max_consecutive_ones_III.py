class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Brute Force Sol
        # TC=O(n**2)  SC=O(1)
        """maxi=0
        n=len(nums)
        for i in range(n):
            zeros=0
            for j in range(i,n):
                if nums[j]==0:
                    zeros+=1
                if zeros>k:
                    break
                maxi=max(j-i+1,maxi)
        return maxi"""

        # Better Sol
        # TC=O(2n)  SC=O(1)
        """l=0
        r=0
        maxi=0
        n=len(nums)
        zeros=0
        while r<n:
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            maxi=max(r-l+1,maxi)
            r+=1
        return maxi"""

        # Optimal Sol-don't make the window smaller than the 1st longest length
        # TC=O(n)  SC=O(1)
        l = 0
        r = 0
        maxi = 0
        n = len(nums)
        zeros = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                maxi = max(r - l + 1, maxi)
            r += 1
        return maxi
