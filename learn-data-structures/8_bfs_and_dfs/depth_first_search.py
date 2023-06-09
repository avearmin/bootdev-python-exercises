# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/35d2354e-1601-42a4-b583-c38a3577e891/0deb238d-8b3c-48b0-a367-caf08d65eed4

class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for neighbor in neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)


        # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


def test(edges_to_add, starting_at):
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("-------------------------------------")
    for v in graph.depth_first_search(starting_at):
        print(f"Visiting: {v} \n")
    print("=====================================")


def main():
    test(
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("Cairo", "Dubai"),
            ("Dubai", "Kyiv"),
        ],
        "New York",
    )
    test(
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "New York",
    )


main()

