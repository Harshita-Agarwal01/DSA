# TC=O(n)  SC=O(1)
class Solution:
    def findMin(self, n: int) -> int:
        # code here
        c = 0
        while n > 0:
            if n >= 10:
                c += 1
                n -= 10
            elif n >= 5:
                c += 1
                n -= 5
            elif n >= 2:
                c += 1
                n -= 2
            else:
                c += 1
                n -= 1

        return c
