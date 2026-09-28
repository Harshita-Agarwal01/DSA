# TC=O(n1logn1)+O(n2logn2)+O(n2)  SC=O(1)
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n1 = len(g)
        n2 = len(s)
        l, r = 0, 0
        c = 0
        while l < n1 and r < n2:
            if g[l] > s[r]:
                r += 1
            else:
                c += 1
                l += 1
                r += 1
        return c
