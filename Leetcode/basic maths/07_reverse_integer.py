# Leetcode- 07- Reverse Integer
# Difficulty- Easy
# Time Complexity: O()
# Space Compexity: O(1)
class Solution(object):
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        num=abs(x)
        result=0
        while num>0:
            ld=num%10
            result= (result*10)+ld
            num=num//10
        if result>2**31-1:
            return 0
        if x>0:
            return result 
        return -result