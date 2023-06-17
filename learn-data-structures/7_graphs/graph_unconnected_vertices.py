# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/b4110935-3415-4e52-9370-d7db0a6d7619/ea912181-9d34-4bd3-abe3-627db20ea7ea

class Graph:
    def unconnected_vertices(self):
        found_unconnected_vertices = []
        for vertex, connections in self.graph.items():
            # In Python, an empty set evaluates to False, while a non-empty set evaluates to True. 
            # So, `if not connections` checks if the connections set is empty. It is also flexible,
            # and would still work if connections were stored in a list.
            if not connections: 
                found_unconnected_vertices.append(vertex)
        return found_unconnected_vertices

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()


def test(edges_to_add, unconnected_nodes_to_add):
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("-------------------------------------")
    for node in unconnected_nodes_to_add:
        graph.add_node(node)
        print(f"Added unconnected node: {node}")
    print("-------------------------------------")
    unconnected = graph.unconnected_vertices()
    print(f"Unconnected vertices: {sorted(unconnected)}")
    print("=====================================")


def main():
    test(
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        [6, 7],
    )
    test(
        [
            (1, 2),
            (1, 3),
        ],
        [0, 4],
    )


main()
