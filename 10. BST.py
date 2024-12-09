from anyio import current_effective_deadline


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add_node(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            if new_node.data < current.data:
                if current.left != None:
                    current.left = new_node
                else:
                    current = current.left
            else:
                if current.right != None:
                    current.right = new_node
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

