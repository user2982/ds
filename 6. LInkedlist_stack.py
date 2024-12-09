from pydoc_data.topics import topics


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return
        self.top = self.top.next

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.top.data

    def display(self):
        if self.is_empty():
            print("stack is empty")
            return
        current = self.top
        while current != None:
            print(current.data, end=" ")
            current = current.next

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.display()
    print("\nAfter popping:")
    stack.pop()
    stack.display()
    print("\nTop element:", stack.peek())

