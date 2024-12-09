class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current= self.head
        while True:
            if current.next == None:
                current.next = new_node
                break
            else:
                current = current.next

    def insert_after(self,data,after_element):
        new_node = Node(data)
        current = self.head
        while current.data != after_element:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        if self.head == None:
            print("Empty")
            return
        current =self.head
        while current is not None:
            print(current.data,end=" ")
            current = current.next
        print()

    def delete_head(self):
        if self.head == None:
            print("Empty")
            return
        self.head = self.head.next

    def delete_tail(self):
        current = self.head
        prev = None
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None

    def delete_node(self,data):
        current = self.head
        prev = None
        while current.data != data and current.next != None:
            prev = current
            current = current.next
        if current.next == None:
            print("Not found")
            return
        prev.next = current.next

if __name__ == "__main__":
    sll = SLL()
    n = int(input())
    for i in range(n):
        val = input().split()
        if int(val[0]) == 1:
            sll.insert_at_beginning(val[1])
        elif int(val[0]) == 2:
            sll.insert_at_end(val[1])
        elif int(val[0]) == 3:
            sll.insert_after(int(val[1]),int(val[2]))
        elif int(val[0]) == 4:
            sll.display()
        elif int(val[0]) == 5:
            sll.delete_tail()
        elif int(val[0]) == 6:
            sll.delete_node(int(val[1]))
        elif int(val[0]) == 7:
            sll.delete_head()