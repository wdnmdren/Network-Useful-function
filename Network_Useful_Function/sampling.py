import random

def snowball_sampling(G, seed_nodes, size, max_wave=2):
    V_s = set(seed_nodes)
    E_s = set()
    current_wave = set(seed_nodes)
    for _ in range(max_wave):
        new_nodes = set()
        for node_i in current_wave:
            for node_j in G.neighbors(node_i):
                if len(V_s) < size:
                    E_s.add((node_i, node_j))
                    new_nodes.add(node_j)
                    V_s.add(node_j)
                else:
                    return V_s
        current_wave.update(new_nodes)
    return V_s

def snowball_sampling_shuffle(G, seed_nodes, size, max_wave=2):
    V_s = set(seed_nodes)
    E_s = set()
    current_wave = set(seed_nodes)

    for _ in range(max_wave):
        potential_edges = []
        new_nodes = set()
        for node_i in current_wave:
            for node_j in G.neighbors(node_i):
                if node_j not in V_s:
                    potential_edges.append((node_i, node_j))
        random.shuffle(potential_edges)
        for node_i, node_j in potential_edges:
            if len(V_s) < size:
                E_s.add((node_i, node_j))
                new_nodes.add(node_j)
                V_s.add(node_j)
            else:
                return V_s
        current_wave.update(new_nodes)
    return V_s
