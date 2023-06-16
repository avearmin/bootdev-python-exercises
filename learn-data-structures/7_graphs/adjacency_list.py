# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/b4110935-3415-4e52-9370-d7db0a6d7619/e9dec025-2a1b-4f24-bfc2-0033c8968e43

class Graph:
    def __init__(self):
        # ?

    def add_edge(self, u, v):
        # ?

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) or (u in self.graph[v])
        return False


def test(edges_to_add, edges_to_test):
    graph = Graph()
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
