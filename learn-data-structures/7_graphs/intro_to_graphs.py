# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/b4110935-3415-4e52-9370-d7db0a6d7619/e2345ef4-f077-40b2-86ed-a30d911f50c8

class Graph:
    def __init__(self, num_vertices):
        # ?

    def add_edge(self, u, v):
        # ?

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]


def test(num_vertices, edges_to_add, edges_to_test):
    graph = Graph(num_vertices)
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("-------------------------------------")
    for edge in edges_to_test:
        exists = graph.edge_exists(edge[0], edge[1])
        print(f"{edge} exists: {exists}")
    print("=====================================")


def main():
    test(
        3,
        [
            (0, 1),
            (2, 0),
        ],
        [
            (1, 0),
            (1, 2),
            (2, 0),
        ],
    )
    test(
        6,
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        [
            (0, 1),
            (1, 2),
            (0, 4),
            (2, 5),
            (5, 0),
        ],
    )


main()
