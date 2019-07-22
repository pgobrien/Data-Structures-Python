# Adjacency List

class AdjacencyList:

    def __init__(self):
        self.internal_dict = {}

    def num_vertices(self):
        return len(self.internal_dict)

    def add_vertex(self, u):
        self.internal_dict[u] = []

    def add_edge(self, u, v):
        self.internal_dict[u].append(v)

    def print_adjacency(self):
        for u, v in self.internal_dict.items():
            print(u, ':', v)

    def vertices(self):
        return self.internal_dict.keys()

    def get_neighbors(self, u):
        return self.internal_dict[u]

# Path between Nodes using a Breadth First Search
def path_between_nodes(s, t, graph):

    queue = [s]
    visited = []
    while queue:
        temp_vertex = queue.pop(0)

        if temp_vertex == t:
            return True

        for neighbor in graph.get_neighbors(temp_vertex):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    return False


if __name__ == '__main__':
    test = AdjacencyList()

    test.add_vertex(0)
    test.add_vertex(1)
    test.add_vertex(2)
    test.add_vertex(3)
    test.add_vertex(4)
    test.add_vertex(5)

    test.add_edge(0, 1)
    test.add_edge(0, 4)
    test.add_edge(0, 5)

    test.add_edge(1, 4)
    test.add_edge(1, 3)

    test.add_edge(2, 1)

    test.add_edge(3, 2)
    test.add_edge(3, 4)

    test.print_adjacency()
    print()
    print(path_between_nodes(0, 3, test))
    print(path_between_nodes(2, 4, test))
    print(path_between_nodes(1, 5, test))





