class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph.get(node, []))
        return result

if __name__ == "__main__":
    g = Graph()

    for i in range(int(input("Enter no.of nodes:"))):
        li = input("Enter node and neighbor separated by a space: ").split()
        g.add(li[0], li[1])

    print(g.bfs("A"))