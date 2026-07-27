# TC=O((2**t) * k) where t is the number of times a single element can be used
# SC=O(2**t) stackspace plus O(k) which is the length of subsets; ignoring result list
class Solution:
    def solve(self,ind,candidates,target,total,subset,result):
        if ind==len(candidates):
            return
        elif total==target:
            result.append(subset.copy())  #TC=O(K) where k is the avg length of an answer
            return
        elif total>target:
            return 
        subset.append(candidates[ind])
        s=total+candidates[ind]
        self.solve(ind,candidates,target,s,subset,result)
        
        e=subset.pop()
        s=s-e
        self.solve(ind+1,candidates,target,s,subset,result)

        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        subset=[]
        self.solve(0,candidates,target,0,subset,result)
        return result