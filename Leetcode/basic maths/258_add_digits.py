class Solution:
    def addDigits(self, num: int) -> int:
        # TC=O(logN)  SC=O(1)
        """while num>=10:
            s=0
            while num>0:
                dig=num%10
                s+=dig
                num=num//10
            num=s
        return num"""

        # TC=O(1)  SC=O(1)
        # Digital Root Concept- the final root digit you get after repeatedly reducing a number by 
        # summing its digits until only one digit remains
        if num==0:
            return 0
        return 1 + (num-1)%9

        