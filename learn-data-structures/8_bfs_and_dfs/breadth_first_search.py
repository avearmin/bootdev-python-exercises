# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/35d2354e-1601-42a4-b583-c38a3577e891/a607653a-92c2-4898-b19f-e5469384a1c6

class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = [v]
        while to_visit: # While to_visit is not empty:
            current_vertex = to_visit.pop(0) # Pop the first vertex off the to_visit list
            visited.append(current_vertex)   # and visit it by appending it to visited.
            neighbors = sorted(self.graph[current_vertex]) # Get a sorted() list of the neighbors of the vertex we just visited.
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited # Once to_visit is empty, we've traversed the whole graph so just return visited.

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
    for v in graph.breadth_first_search(starting_at):
        print(f"Visiting: {v} \n")
    print("=====================================")


def main():
    test(
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
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
