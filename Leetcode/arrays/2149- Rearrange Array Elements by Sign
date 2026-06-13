class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Brute Force sol
        # TC=O(N+N/2)  SC=O(N)
        """n=len(nums)
        pos,neg=[],[]
        for i in range(n):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[(2*i)+1]=neg[i]
              
        return nums"""

        # Optimal sol- Two pointer
        #TC=O(N)   
        #SC=O(N) if we consider result but it is the answer itself thus we can consider O(1)

        n=len(nums)
        result=[0]*n    #also takes O(N) TC but is ignored
        pos=0
        neg=1

        for i in range(n):
            if nums[i]>=0:
                result[pos]=nums[i]
                pos+=2
            else:
                result[neg]=nums[i]
                neg+=2
        return result
        