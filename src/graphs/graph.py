import heapq
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
