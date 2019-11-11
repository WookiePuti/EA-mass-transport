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
################################################################





#tworzenie grafu polaczen:


graph_struct = np.array([(1, 2, 1), (2, 3, 2), (1, 3, 4), (3, 4, 4), (4, 2, 3)])   #example structure
route_graph = nx.DiGraph()
route_graph.add_weighted_edges_from(graph_struct)

# tworzenie populacji startowej
def create_first_pop(route, num_of_bus=1):
    pass



