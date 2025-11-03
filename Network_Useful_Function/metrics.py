import networkx as nx
from itertools import combinations

def modularity(G, partition):
    if G.number_of_edges() == 0:
        return 0.0

    weighted = nx.is_weighted(G)
    m = G.size(weight="weight") if weighted else G.number_of_edges()

    node_to_comm = {}
    for idx, comm in enumerate(partition):
        for node in comm:
            node_to_comm[node] = idx

    total_sum = 0.0
    for i, j in combinations(G.nodes(), 2):
        if node_to_comm.get(i) != node_to_comm.get(j):
            continue
        A_ij = G[i][j].get("weight", 1.0) if weighted and G.has_edge(i,j) else (1.0 if G.has_edge(i,j) else 0.0)
        k_i = G.degree(i, weight="weight") if weighted else G.degree(i)
        k_j = G.degree(j, weight="weight") if weighted else G.degree(j)
        total_sum += (A_ij - (k_i * k_j) / (2 * m))

    Q = total_sum / (2 * m)
    return Q
