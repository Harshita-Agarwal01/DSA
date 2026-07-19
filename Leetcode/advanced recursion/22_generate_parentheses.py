class Solution:
    def solve(self,n,index,op,close,string,result):
        if index==(2*n):
            result.append("".join(string))
        if op<n:
            string[index]="("
            self.solve(n,index+1,op+1,close,string,result)
        if close<op:
            string[index]=")"
            self.solve(n,index+1,op,close+1,string,result)
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        string=[""]*(2*n)
        result=[]
        return self.solve(n,0,0,0,string,result)