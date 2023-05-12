from typing import List
import random
from graphs.graph import Graph, dfs, bfs
from graphs.profiler import plot_result


def complete_binary_tree():
    g = Graph(15)
    for i in range(7):
        g.add_edge(i, 2 * i + 1)
        g.add_edge(i, 2 * i + 2)
    return g


def balanced_tree():
    g = Graph(16)
    for i in range(7):
        g.add_edge(i, 2 * i + 1)
        g.add_edge(i, 2 * i + 2)
    g.add_edge(7, 15)
    return g


def graph_with_cycle():
    g = Graph(16)
    edges = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (0, 8), (8, 9), (9, 10), (8, 11), (11, 12),
             (10, 13), (12, 14), (13, 15), (14, 15)]
    for u, v in edges:
        g.add_edge(u, v)
    return g


def disconnected_graph():
    g = Graph(16)
    for i in range(7):
        g.add_edge(i, 2 * i + 1)
        g.add_edge(i, 2 * i + 2)
    for i in range(7, 11):
        g.add_edge(i, 2 * (i - 7) + 8)
        g.add_edge(i, 2 * (i - 7) + 9)
    return g


# Test Case 7: A balanced tree with 31 vertices (4 levels)

def balanced_tree_vertices():
    g = Graph(31)
    for i in range(15):
        g.add_edge(i, 2 * i + 1)
        g.add_edge(i, 2 * i + 2)
    return g


# Test Case 8: A more complex graph with multiple cycles and branches

def complex_graph_with_cycles():
    g = Graph(18)
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (2, 7),
        (3, 8), (8, 9), (4, 9),
        (5, 10), (10, 11), (6, 11),
        (10, 14), (11, 15), (14, 15),
        (8, 12), (12, 13), (9, 13),
        (12, 16), (13, 17), (16, 17)
    ]
    for u, v in edges:
        g.add_edge(u, v)
    return g


def run_test(func, name):
    print(name + ':')
    bfs(func(), 0)
    dfs(func(), 0)
    print('---')


def generate_random_graph(N, edge_probability=0.5):
    g = Graph(N)
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < edge_probability:
                g.add_edge(i, j)

    return g


def main() -> int:
    run_test(complete_binary_tree, 'Complete binary tree')
    run_test(balanced_tree, 'Balanced Tree')
    run_test(graph_with_cycle, 'Graph with Cycles')
    run_test(disconnected_graph, 'Disconnected graph')
    run_test(balanced_tree_vertices, 'Balanced tree with lots of vertices')
    run_test(complex_graph_with_cycles, 'Complex graph with cycles and multiple branches')
    # plot_result(
    #     ['complete_binary_tree', 'balanced_tree', 'graph_with_cycle', 'disconnected_graph', 'balanced_tree_vertices',
    #      'complex_graph_with_cycles'])
    # inp = []
    # for _ in range(50, 1000, 100):
    #     random_graph = generate_random_graph(_)
    #     print(_)
    #     dfs(random_graph, 0)
    #     bfs(random_graph, 0)
    #     inp.append(_)
    #
    # plot_result(inp)
    return 0


main()
