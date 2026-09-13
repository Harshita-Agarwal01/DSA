"""Structure of linked list Node
class Node:
   def __init__(self, val):
       self.data = val
       self.next = None
"""


class myStack:

    def __init__(self):
        # Initialize your data members
        self.head = None
        self.count = 0

    def isEmpty(self):
        # Check if the stack is empty
        return self.head == None

    def push(self, x):
        # Adds element x to the top of the stack
        new_Node = Node(x)
        new_Node.next = self.head
        self.head = new_Node
        self.count += 1

    def pop(self):
        # Removes an element from the top of the stack
        if self.head == None:
            return

        else:
            self.head = self.head.next
            self.count -= 1

    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.head == None:
            return -1
        return self.head.data

    def size(self):
        # Returns the current size of the stack
        return self.count
