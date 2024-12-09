class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        result = [start]

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))

        return result

if __name__ == "__main__":
    g = Graph()

    for i in range(int(input("Enter no.of nodes:"))):
        li = input("Enter node and neighbor separated by a space: ").split()
        g.add(li[0], li[1])

    print(g.dfs("A"))