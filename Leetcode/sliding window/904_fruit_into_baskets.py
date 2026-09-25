class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Brute Force sol
        # TC=O(n**2)  SC=O(3) bcz len of set cannot go above 3
        """n=len(fruits)
        maxi=0
        for i in range(n):
            my_set=set()
            for j in range(i,n):
                my_set.add(fruits[j])
                if len(my_set)>2:
                    break
                maxi=max(maxi,j-i+1)
        return maxi"""

        # Better sol
        # TC=O(2n)  SC=O(3)
        """n=len(fruits)
        l=0
        r=0
        maxi=0
        freq=dict()
        while r<n:
            freq[fruits[r]]=freq.get(fruits[r],0)+1
            while len(freq)>2:
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1

        return maxi"""

        # Optimal sol
        # TC=O(n)  SC=O(3)
        n = len(fruits)
        l = 0
        r = 0
        maxi = 0
        freq = dict()
        while r < n:
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1
            if len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
            if len(freq) <= 2:
                maxi = max(maxi, r - l + 1)
            r += 1

        return maxi
