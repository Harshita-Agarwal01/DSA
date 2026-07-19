class Solution:
    def generate(self,index,numbers,result):
        if index==len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="0"
        self.generate(index+1,numbers,result)
        numbers[index]="1"
        self.generate(index+1,numbers,result)
        return result
                
            
    def binstr(self, n):
        # code here
        result=[]
        numbers=["0"]*n
        return self.generate(0,numbers,result)