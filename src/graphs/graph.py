from collections import deque
from .profiler import exec_time

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(self.vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

def dfs_recursive(graph: Graph, start_vertex, visited):
    visited[start_vertex] = True
    print(start_vertex, end=' ')

    for vertex in graph.adj_list[start_vertex]:
        if not visited[vertex]:
            dfs_recursive(graph, vertex, visited)

@exec_time("dfs")
def dfs(graph: Graph, start_vertex) -> any:
    print("dfs: ", end="")
    visited = [False] * graph.vertices
    dfs_recursive(graph, start_vertex, visited)

@exec_time("bfs")
def bfs(graph: Graph, start_vertex) -> any:
    visited = [False] * graph.vertices

    # Create a queue for BFS and enqueue the start_vertex
    queue = deque([start_vertex])

    # Mark the start_vertex as visited
    visited[start_vertex] = True
    print("bfs: ", end="")
    while queue:
        # Dequeue a vertex from the queue and print it
        current_vertex = queue.popleft()
        print(current_vertex, end=' ')

        # Get all adjacent vertices of the dequeued vertex
        for vertex in graph.adj_list[current_vertex]:
            # If the adjacent vertex is not visited, mark it as visited and enqueue it
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
