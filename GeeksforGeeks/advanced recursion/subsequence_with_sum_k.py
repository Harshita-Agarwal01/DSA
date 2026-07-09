class Solution:
    def solve(self,index,total,arr,k):
        if index>=len(arr):
            if total==k:
                return True
            return False
        elif total>k:
            return False
        curr_sum=total+arr[index]
        pick=self.solve(index+1,curr_sum,arr,k)
        if pick==True:
            return True
        curr_sum=total
        not_pick=self.solve(index+1,curr_sum,arr,k)
        return not_pick
        
    def checkSubsequenceSum(self, arr, k):
        # code here
        index=0
        total=0
        return self.solve(index,total,arr,k)
        