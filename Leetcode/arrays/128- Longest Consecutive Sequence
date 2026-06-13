class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Sorting based solution
        # TC=O(NLOGN + N)       SC=O(1)
        """nums.sort()             #O(NLOGN)
        n=len(nums)
        count=1
        final_count=1
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(1,n):        #O(N)
            
            if nums[i]==nums[i-1]+1:
                count+=1
            
                if count>final_count:
                    final_count=count
            elif nums[i]==nums[i-1]:
                continue
            else:
                count=1

        return final_count"""


        # Optimal sol- using set
        # TC=O(3N)~O(N)    SC=O(N)
        my_set=set()
        n=len(nums)
        for i in range(n):
            my_set.add(nums[i])
        longest=0
        for i in my_set:
            
            if i-1 not in my_set:
                num=i
                count=1
                while num+1 in my_set:
                    count+=1
                    num+=1
                longest=max(longest,count)
        return longest