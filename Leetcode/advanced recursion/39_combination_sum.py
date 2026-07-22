class Solution:
    def solve(self,ind,candidates,target,total,subset,result):
        if ind==len(candidates):
            return
        elif total==target:
            result.append(subset.copy())
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