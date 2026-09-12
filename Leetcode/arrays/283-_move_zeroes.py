class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #Brute force solution      TC=O(2N)~O(N)  SC=O(N)
        """temp=[]                                 
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
        nl=len(temp)
        for j in range(nl):
            nums[j]=temp[j]
       
        for i in range(nl,n):
            nums[i]=0"""
        
        #Optimal solution      TC=O(N)  SC=O(1)
        i=0
        n=len(nums)
        if n==1:
            return
        while i<n:
            if nums[i]==0:
                break
            i+=1
        if i==n:
            return
        j=i+1
        while j<n:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1