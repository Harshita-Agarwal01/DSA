# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Queue class template
class myQueue:
    def __init__(self):
        # Initialize your data members
        self.head = None
        self.curr = None
        self.length = 0

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.head == None

    def enqueue(self, x):
        # Add element x to the rear
        new_Node = Node(x)
        if self.head == None:
            self.head = new_Node
            self.curr = new_Node
        else:
            self.curr.next = new_Node
            self.curr = new_Node
        self.length += 1

    def dequeue(self):
        # Remove the front element
        if self.head == None:
            return
        else:
            self.head = self.head.next
        self.length -= 1
        if self.head == None:
            self.curr = None

    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.head == None:
            return -1
        return self.head.data

    def size(self):
        # Return current size
        return self.length
