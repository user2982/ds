class Queue:
    def __init__(self):
        self.arr = []

    def enrear(self,data):
        return self.arr.append(data)

    def derear(self):
        return self.arr.pop()

    def enfront(self,data):
        return self.arr.insert(0,data)

    def defront(self):
        return self.arr.pop(0)

    def rearpeek(self):
        return self.arr[-1]

    def frontpeek(self):
        return self.arr[0]

    def display(self):
        return len(self.arr)

q = Queue()
n = int(input())
for i in range(n):
    oper = input().split()
    if len(oper)>=2:
        op = oper[0]
        data = oper[1]

        if op == "append":
            q.enrear(data)
        elif op == "appendleft":
            q.enfront(data)
        elif op == "pop":
            print(q.derear())
        elif op == "popleft":
            print(q.defront())
        elif op == "peek":
            print(q.rearpeek())
        elif op == "peekleft":
            print(q.frontpeek())
        elif op == "size":
            q.display()
