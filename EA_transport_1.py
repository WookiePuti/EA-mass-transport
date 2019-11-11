import numpy as np
import networkx as nx
import matplotlib as plt

from obj_fun import obj_fun
from Crossover_operator import crossover_oper

###################################
# TODO
# tworzenie populacji startowej
# funkcja celu
# Operator krzyzowania
# Operator mutacji
#######################################





#paramentry  symulacji

num_of_obj_fun = None   #liczba wywolan funkcji celu
stop_cond = None        #warunek stopu
start_pop_size = None   #liczebnosc poczatkowej populacji
################################################################





#tworzenie grafu polaczen:
# v 0.1 mamy n wierzcholkow, kazdy jest polaczony z kazdym


graph_struct = np.array([(1, 2, 1), (2, 3, 2), (1, 3, 4), (3, 1, 4), (3, 2, 3), (2, 1, 2)])   #example structure
route_graph = nx.DiGraph()
route_graph.add_weighted_edges_from(graph_struct)


#tworzenie macierzy opisujacej cele podrozy pasazerow

def create_dest_mat(n, b_stop_capacity=20):
    passenger_counter = 0
    mat = np.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i != j:
                mat[i, j] = np.random.randint(0, (b_stop_capacity-passenger_counter))
                passenger_counter += mat[i, j]

    return mat


#tworzenie losowego rozwiazania
# v 0.1 zakladamy ze n=1 to startowy i koncowy, przechodzac do nastepnego wierzcholak losujemy z sukcesorow

def create_rand_sol(route: nx.DiGraph, num_of_bus=1, default_start_node=1):
    sol = np.zeros((num_of_bus, (route.number_of_nodes()+1)), dtype=int)
    for bus in range(num_of_bus):
        sol[num_of_bus-1, 0] = default_start_node
        sol[num_of_bus-1, route.number_of_nodes()] = 1
        actual_node = 1
        for node in range(route.number_of_nodes()-1):
            temp_succesors = list(route.successors(actual_node))
            actual_node = temp_succesors[np.random.randint(0, (len(temp_succesors)-1))]
            sol[num_of_bus-1, node+1] = actual_node
    return sol



# tworzenie populacji startowej
def create_first_pop(route, amount_of_pop):
    population = np.array([])
    for solution in range(amount_of_pop):
        population = np.append(population, create_rand_sol(route))
    return population


c1 = create_first_pop(route_graph, 10)
print(c1)


