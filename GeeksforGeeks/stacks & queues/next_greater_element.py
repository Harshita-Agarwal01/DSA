# Monotonic Stack=elements are kept in either asc or desc order
# TC=O(n) [Amortized analysis]  SC=O(n)
class Solution:
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        ans=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans