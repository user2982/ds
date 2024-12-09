# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}
#
#     def add_node(self, node):
#         if node not in self.adjacency_list:
#             self.adjacency_list[node] = []
#
#     def add_vertices(self, node1, node2):
#             if node1 in self.adjacency_list and node2 in self.adjacency_list:
#                 self.adjacency_list[node1].append(node2)
#                 self.adjacency_list[node2].append(node1)
#                 return
#             if node1 in self.adjacency_list:
#                 self.adjacency_list[node1].append(node2)
#
#     def display(self):
#         for node, neighbor in self.adjacency_list.items():
#             print(f"{node}: {neighbor}")
#
# if __name__ == "__main__":
#     graph = Graph()
#
#     n = int(input("Enter the number of node: "))
#     for i in range(n):
#         node = input("Enter the nodes:")
#         graph.add_node(node)
#
#     o = int(input("Enter number of edges: "))
#     for i in range(o):
#         m = input("Enter the node and edge separeted by coma: ").split()
#         vertex = m[0]
#         edge = m[1]
#         graph.add_vertices(vertex, edge)
#
#     print("Adjacency List:")
#     graph.display()

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_vertices(self, node1, node2):
            if node1 in self.adjacency_list and node2 in self.adjacency_list:
                self.adjacency_list[node1].append(node2)
                self.adjacency_list[node2].append(node1)
                return
            if node1 in self.adjacency_list:
                self.adjacency_list[node1].append(node2)

    def display(self):
        for node, neighbor in self.adjacency_list.items():
            print(f"{node}: {neighbor}")

if __name__ == "__main__":
    graph = Graph()

    n = int(input("Enter the number of node: "))
    for i in range(n):
        node = input("Enter the nodes:")
        graph.add_node(node)

    o = int(input("Enter number of edges: "))
    for i in range(o):
        m = input("Enter the node and edge separeted by coma: ").split()
        vertex = m[0]
        edge = m[1]
        weight = m[2]
        graph.add_vertices(vertex, edge)

    print("Adjacency List:")
    graph.display()
