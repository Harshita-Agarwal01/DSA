class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.items = []
        self.size = n

    def isEmpty(self):
        # Check if stack is empty
        return len(self.items) == 0

    def isFull(self):
        # Check if stack is full
        return len(self.items) == self.size

    def push(self, x):
        # Insert x at the top of the stack
        self.items.append(x)

    def pop(self):
        # Removes an element from the top of the stack
        if len(self.items) == 0:
            return
        self.items.pop()

    def peek(self):
        # Returns the top element of the stack
        if len(self.items) == 0:
            return -1
        return self.items[-1]
