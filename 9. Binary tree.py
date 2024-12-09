class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.left == None:
                temp.left = new_node
                break
            else:
                queue.append(temp.left)
            if temp.right == None:
                temp.right = new_node
                break
            else:
                queue.append(temp.right)

    def display(self):
        print("Tree built successfully")

if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(int(input())):
        val = int(input())
        tree.add(val)
    tree.display()
