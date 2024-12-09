class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack)==0

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack underflow")
        return self.stack[-1]

if __name__ == "__main__":
    stack = Stack()
    n = int(input())
    for i in range(n):
        val = input().split()
        if val[0] == "push":
            stack.push(val[1])
            print(f"{val[1]} is added to the stack")
        elif val[0] == "pop":
            result = stack.pop()
            print(f"{result} has removed form stack")
        elif val[0] == "peek":
            print("Top element:",stack.peek())


