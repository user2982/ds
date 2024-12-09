class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return value

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue:", end=" ")
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size
        print()

cq = CircularQueue(3)
n = int(input())
for i in range(n):
    val = input().split()
    if val[0] == "ENQUEUE":
        cq.enqueue(val[1:])
    elif val[0] == "DEQUEUE":
        cq.dequeue()
cq.display()
