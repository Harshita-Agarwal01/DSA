class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force Sol
        # TC=O(n**2)  SC=O(n)
        """maxi=0
        n=len(s)
        for i in range(n):
            my_set=set()
            for j in range(i,n):
                if s[j] in my_set:
                    break
                maxi=max(maxi,j-i+1)
                my_set.add(s[j])
        return maxi"""

        # Optimal Sol-Sliding Window & Two Pointers
        # TC=O(n)  SC=O(n)
        maxi = 0
        n = len(s)
        l = 0
        r = 0
        my_dict = dict()
        while r < n:
            if s[r] in my_dict:
                l = max(l, my_dict[s[r]] + 1)

            my_dict[s[r]] = r
            maxi = max(maxi, r - l + 1)
            r += 1
        return maxi
