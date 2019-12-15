import numpy as np
import networkx as nx


#tworzenie macierzy opisujacej cele podrozy pasazerow

def create_dest_mat(n, b_stop_capacity=20):

    mat = np.zeros((n, n))
    for i in range(n):
        passenger_counter = 0
        for j in range(n):
            if i != j:
                mat[i, j] = np.random.randint(0, (b_stop_capacity-passenger_counter))
                passenger_counter += mat[i, j]

    return mat

def create_route_complete_graph(num_of_nodes, max_route_weight=10):
    graph = nx.complete_graph(num_of_nodes)
    for (node1, node2) in graph.edges():
        graph.edges[node1,node2]['weight'] = np.random.randint(1, max_route_weight)
    graph = nx.relabel_nodes(graph, lambda x: x + 1, copy=False)
    return graph

def create_new_dest_mat_file(num_of_bus_stop, file_name='dest_mat.csv', bus_stop_capacity=20):
    np.savetxt(file_name, create_dest_mat(num_of_bus_stop, bus_stop_capacity), delimiter=',')


def load_dest_mat_from_file(file_name='dest_mat.csv'):
    return np.loadtxt(file_name, delimiter=',')


def create_to_file_graph(num_of_nodes, filename="route_graph.edgelist", max_route_weight=10):
    G = create_route_complete_graph(num_of_nodes, max_route_weight)
    nx.write_weighted_edgelist(G, filename)


def load_route_graph_from_file(file_name="route_graph.edgelist"):
    return nx.read_weighted_edgelist(file_name, nodetype=int)



