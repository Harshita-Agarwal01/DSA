class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.items = []
        self.size = n

    def isEmpty(self):
        # Check if queue is empty
        return len(self.items) == 0

    def isFull(self):
        # Check if queue is full
        return len(self.items) == self.size

    def enqueue(self, x):
        # Enqueue
        if len(self.items) == self.size:
            return
        else:
            self.items.append(x)

    def dequeue(self):
        # Dequeue
        if len(self.items) == 0:
            return
        else:
            self.items.pop(0)

    def getFront(self):
        # Get front element
        if len(self.items) == 0:
            return -1
        else:
            return self.items[0]

    def getRear(self):
        # Get rear element
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]
