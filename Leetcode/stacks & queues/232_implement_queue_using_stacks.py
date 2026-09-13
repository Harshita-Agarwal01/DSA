# TC=O(n)  # SC=O(n)
class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x: int) -> None:   # TC=O(2n)
        while self.st1:               # TC=O(n)
            self.st2.append(self.st1.pop())
        self.st2.append(x)
        while self.st2:               # TC=O(n)
            self.st1.append(self.st2.pop())

    def pop(self) -> int:             # TC=O(1)
        if len(self.st1)==0:
            return 
        return self.st1.pop()
        
    def peek(self) -> int:            # TC=O(1)
        if len(self.st1)==0:
            return 
        return self.st1[-1]

    def empty(self) -> bool:
        return len(self.st1)==0
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()