class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TC=O(N)  SC=O(N)
        """n=len(s)
        lst=[]
        for i in range(n):
            if s[i].isalnum():
                lst.append(s[i].lower())
        length=len(lst)
        l=0
        r=length-1
        while l<r:
            if lst[l]!=lst[r]:
                return False
            l+=1
            r-=1
        return True"""

        # TC=O(N)  SC=O(1)
        n=len(s)
        l=0
        r=n-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
            