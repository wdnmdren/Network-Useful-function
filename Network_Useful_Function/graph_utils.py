def all_shortest_from(G, node_i):
    """
    BFS shortest path lengths from node_i to all others.
    """
    if node_i not in G:
        raise ValueError(f"Node {node_i} not in graph")

    distances = {}
    visited = set([node_i])
    queue = [(node_i, 0)]

    while queue:
        current, length = queue.pop(0)
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = length + 1
                queue.append((neighbor, length + 1))

    for n in G.nodes():
        if n not in distances and n != node_i:
            distances[n] = -1

    return distances
