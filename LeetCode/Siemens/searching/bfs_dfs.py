import networkx as nx
from matplotlib import pyplot as plt


def dfs(graph, start_node):
    sequence = []

    dfs = []
    dfs.append(start_node)
    seen = set()
    seen.add(start_node)

    while dfs:
        focus_node = dfs.pop()
        sequence.append(focus_node)

        for neigh in graph.neighbors(focus_node):
            if neigh not in seen:
                dfs.append(neigh)
                seen.add(neigh)

    return sequence


def bfs(graph, start_node):
    queue = []
    seen = set()

    sequence = []

    focus_node = start_node

    queue.append(focus_node)
    seen.add(focus_node)

    while queue:
        focus_node = queue.pop(0)
        sequence.append(focus_node)

        for neigh in graph.neighbors(focus_node):

            if neigh not in seen:
                queue.append(neigh)
                seen.add(neigh)
    return sequence


def show_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, with_labels=True,  pos=pos)
    plt.show()


if __name__ == '__main__':
    network = ""
    graph = nx.erdos_renyi_graph(12, 0.25, seed=42)

    show_graph(graph)

    bfs_seq = bfs(graph, 0)
    dfs_seq = dfs(graph, 0)

    print("BFS: ", bfs_seq)
    print("DFS: ", dfs_seq)
    # BFS Seguence:  [0, 2, 4, 8, 10, 11, 5, 9, 1, 7, 6, 3]
    # DFS Seguence:  [0, 11, 10, 7, 6, 5, 1, 3, 8, 4, 9, 2]
