class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self,data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            current = self.front
            while current.next != None:
                current = current.next
            current.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        self.front = self.front.next

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while current != None:
            print(current.data,end=" ")
            current = current.next

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.display()
    print("\nAfter removing the first element: ")
    queue.dequeue()
    queue.display()