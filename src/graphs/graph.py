import heapq
from collections import defaultdict

from .profiler import exec_time


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(self.vertices)}

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))


@exec_time("floyd_warshall")
def floyd_warshall(graph, start):
    # Initialize the distance matrix with infinity for all pairs
    distances = [[float('inf')] * graph.vertices for _ in range(graph.vertices)]

    # Set the distance of each vertex to itself as 0
    for vertex in range(graph.vertices):
        distances[vertex][vertex] = 0

    # Populate the distance matrix with direct edges
    for vertex, neighbors in graph.adj_list.items():
        for neighbor, weight in neighbors:
            distances[vertex][neighbor] = weight
            distances[neighbor][vertex] = weight

    # Dynamic programming - Floyd-Warshall algorithm
    for k in range(graph.vertices):
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances[start]


@exec_time("dijkstra")
def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity except the start vertex
    distances = [float('inf')] * graph.vertices
    distances[start] = 0

    # Priority queue to store vertices and their distances
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Skip if the current distance is greater than the stored distance
        if current_distance > distances[current_vertex]:
            continue

        # Dynamic programming - Dijkstra's algorithm
        for neighbor, weight in graph.adj_list[current_vertex]:
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


@exec_time("kruskal")
def kruskal(graph, start):
    result = []  # This will store the resultant MST
    edges = []

    # Create a list of all edges in the graph
    for node in graph.adj_list:
        for neighbor, weight in graph.adj_list[node]:
            edges.append((weight, node, neighbor))

    # Sort all the edges in non-decreasing order of their weight
    edges.sort()

    parent = [i for i in range(graph.vertices)]

    for edge in edges:
        weight, u, v = edge
        parent_u = find(parent, u)
        parent_v = find(parent, v)
        if parent_u != parent_v:
            result.append((u, v, weight))
            parent[parent_u] = parent_v

    return result


@exec_time("prim")
def prim(graph, start_vertex):
    mst = defaultdict(set)
    visited = set([start_vertex])
    edges = [
        (cost, start_vertex, to)
        for to, cost in graph.adj_list[start_vertex]
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost2 in graph.adj_list[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (cost2, to, to_next))

    return mst
