# exercise link: https://boot.dev/course/7bbb53ed-2106-4f6b-b885-e7645c2ff9d8/35d2354e-1601-42a4-b583-c38a3577e891/c0803659-7811-44fd-a532-3baf926fe435

class Graph:
    def bfs_path(self, start, end):
        visited = [] 
        to_visit = [start] # Queue of vertices to be visited.
        parents = {start: None} # Keep track of which children belong to which parents
        
        while to_visit:  # While to_visit is not empty:
            vertex = to_visit.pop(0) # Pop the first vertex off the queue
            visited.append(vertex)   # and visit it by appending it to visited.
            
            if vertex == end: # If the vertex is `end`,
                path = []     # we intalize our path list.
                while vertex != None:
                    path.insert(0, vertex) # We insert the vertex to the front of the path list
                    vertex = parents[vertex] # Our next vertex becomes the parent of the old one
                return path # We have found the shortest path and return it
            
            neighbours = sorted(self.graph[vertex]) # Get a sorted() list of the neighbors of the vertex we just visited.
            for neighbour in neighbours:
                if neighbour not in visited and neighbour not in to_visit:
                    to_visit.append(neighbour)
                    parents[neighbour] = vertex # Each neighbour added to the queue store a reference to its parent

        return None # If we get here, then we never found `end` and return None

    # don't touch below this line

    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbours = sorted(self.graph[s])
            for neighbour in sorted_neighbours:
                if neighbour not in visited and neighbour not in to_visit:
                    to_visit.append(neighbour)
        return visited

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


def test(edges_to_add, from_vertex, to_vertex):
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    path = graph.bfs_path(from_vertex, to_vertex)
    print("-------------------------------------")
    print(f"Path from {from_vertex} to {to_vertex}: {path}")
    print("=====================================")


def main():
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
        "Cairo",
        "San Francisco",
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
        "Dubai",
    )


main()
