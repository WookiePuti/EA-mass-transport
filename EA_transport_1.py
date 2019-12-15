import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from copy import deepcopy

from obj_fun import obj_fun
from Selection import selection
from Crossover_operator import crossover_oper
from Mutation import mutate1, mutate2
from Simulation import simulate_EA
from Visualize import visualize_best_route
from IO_from_file import create_new_dest_mat_file, load_dest_mat_from_file, create_to_file_graph, load_route_graph_from_file

###################################
# TODO
# tworzenie populacji startowej ////////// no chyba done LP
# funkcja celu
# Metoda selekcji
# Operator krzyzowania
# Operator mutacji
#######################################





#paramentry  symulacji

num_of_obj_fun = 100   #liczba wywolan funkcji celu
stop_cond = None        #warunek stopu
start_pop_size = 100    #liczebnosc poczatkowej populacji
mutate_prob = 0.6
################################################################





#tworzenie grafu polaczen:
# v 0.1 mamy n wierzcholkow, kazdy jest polaczony z kazdym


graph_struct = np.array([(1, 2, 1), (2, 3, 2), (1, 3, 4)])   #example structure
route_graph = nx.Graph()
route_graph.add_weighted_edges_from(graph_struct)





#tworzenie losowego rozwiazania
# v 0.1 zakladamy ze n=1 to startowy i koncowy, przechodzac do nastepnego wierzcholak losujemy z sukcesorow

def create_rand_sol(route: nx.Graph, max_num_of_bus=3, min_route_length=2):
    sol = []
    num_of_bus = np.random.randint(1, max_num_of_bus+1)
    for bus in range(num_of_bus):
        sol.append([])
        route_length = np.random.randint(min_route_length, route.number_of_nodes()+1)
        actual_node = np.random.randint(1, route.number_of_nodes())
        for node in range(route_length):
            temp_neighbors = list(route.neighbors(actual_node))
            actual_node = temp_neighbors[np.random.randint(0, len(temp_neighbors))]
            sol[bus].append(actual_node)
    return sol



# tworzenie populacji startowej
def create_first_pop(route, amount_of_pop):
    population = []
    for solution in range(amount_of_pop):
        population.append(create_rand_sol(route))
    return population


mat = load_dest_mat_from_file()
c1 = create_first_pop(route_graph, 10)

#print(simulate_EA(route_graph, start_pop_size, mat, mutate_prob))

s1 = [[1,2,3]]
s2 =  [[2,3]]
#print(s1,s2)
#print(crossover_oper(s1,s2, route_graph))
create_to_file_graph(10)
route_graph = load_route_graph_from_file()
best_sol = simulate_EA(route_graph, start_pop_size, mat, mutate_prob, num_of_obj_fun)
print(best_sol)



#print(route_graph.edges([1,2]))

visualize_best_route(route_graph, best_sol)
