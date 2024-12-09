class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.data < current.data:
                    if current.left == None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = new_node
                        break
                    else:
                        current = current.right


    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

if __name__ == "__main__":
    bst = BST()
    for i in range(int(input())):
        val = int(input())
        bst.add(val)
    bst.inorder(bst.root)
