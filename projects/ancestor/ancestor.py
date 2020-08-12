from util import Stack, Queue


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex Does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])

    q = Queue()
    q.enqueue(starting_node)
    visited = set()
    earliest = []

    while q.size() > 0:
        current = q.dequeue()
        if current not in visited:
            visited.add(current)
            neighbors = graph.get_neighbors(current)
            for neighbor in neighbors:
                q.enqueue(neighbor)
                earliest.append(neighbor)
    if earliest:
        return earliest[-1]
    else:
        return -1

    # guided solution

    # graph = Graph()
    # for pair in ancestors:
    #     graph.add_vertex(pair[0])
    #     graph.add_vertex(pair[1])
    #     graph.add_edge(pair[1], pair[0])

    # # Do a BFS sotring the path
    # q = Queue()
    # q.enqueue([starting_node])
    # max_path_length = 1
    # earliest_ancestor = -1

    # while q.size() > 0:
    #     path = q.dequeue()
    #     v = path[-1]
    #     if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
    #         earliest_ancestor = v
    #         max_path_length = len(path)
    #         for neighbor in graph.vertices[v]:
    #             path_copy = list(path)
    #             path_copy.append(neighbor)
    #             q.enqueue(path_copy)

    # return earliest_ancestor
