from typing import List
from copy import deepcopy

import numpy as np
import networkx as nx

#koniec pierszego krzyzuje z poczatkiem drugiego robie swap i wstawiam w polaczeniach dijkstre

'''
def crossover_oper(sol_1: List, sol_2: List, route: nx.Graph):
    sol_1_temp = deepcopy(sol_1)
    sol_2_temp = deepcopy(sol_2)
    idx_route2cross1 = np.random.randint(len(sol_1))
    idx_route2cross2 = np.random.randint(len(sol_2))
    exch_len = np.random.randint(1, min(len(sol_1[idx_route2cross1]), len(sol_2[idx_route2cross2]))+1)
    print(exch_len)
    temp_cross_route = deepcopy(sol_1[idx_route2cross1][len(sol_1[idx_route2cross1])-exch_len:])
    sol_1_temp[idx_route2cross1][len(sol_1[idx_route2cross1])-exch_len:] = sol_2[idx_route2cross2][: exch_len]
    sol_2_temp[idx_route2cross2][: exch_len] = temp_cross_route
 
    if sol_1_temp[idx_route2cross1][len(sol_1[idx_route2cross1])-exch_len] not in list(route.neighbors(sol_1[idx_route2cross1][len(sol_1[idx_route2cross1])-exch_len-1])):
        sol_1_temp[idx_route2cross1][len(sol_1[idx_route2cross1])-exch_len:len(sol_1[idx_route2cross1])-exch_len] = nx.dijkstra_path(route, sol_1_temp[idx_route2cross1][len(sol_1[idx_route2cross1])-exch_len], sol_1_temp[len(sol_1[idx_route2cross1])-exch_len+1])[1:-1]
    if sol_2_temp[idx_route2cross2][exch_len+1] not in list(route.neighbors(sol_2[idx_route2cross2][exch_len])):
        sol_2_temp[idx_route2cross2][exch_len:exch_len] = nx.dijkstra_path(route, sol_2_temp[idx_route2cross2][exch_len], sol_2_temp[idx_route2cross2][exch_len+1])[1:-1]

    return [sol_1_temp, sol_2_temp]
'''


def crossover_oper(sol_1: List, sol_2: List, route: nx.Graph):
    sol_1_temp = deepcopy(sol_1)
    sol_2_temp = deepcopy(sol_2)
    idx_route2cross1 = np.random.randint(len(sol_1))
    idx_route2cross2 = np.random.randint(len(sol_2))
    exch_len = 1#np.random.randint(1, min(len(sol_1[idx_route2cross1]), len(sol_2[idx_route2cross2]))+1)
    temp_cross_route = deepcopy(sol_1[idx_route2cross1][len(sol_1[idx_route2cross1]) - exch_len:])
    sol_1_temp[idx_route2cross1][-exch_len:] = sol_2[idx_route2cross2][: exch_len]
    sol_2_temp[idx_route2cross2][: exch_len] = temp_cross_route
    if exch_len < len(sol_1_temp[idx_route2cross1]) :
        if sol_1_temp[idx_route2cross1][-exch_len] not in list(route.neighbors(sol_1_temp[idx_route2cross1][-exch_len-1])):
            if sol_1_temp[idx_route2cross1][-exch_len] == sol_1_temp[idx_route2cross1][-exch_len-1]:
                del sol_1_temp[idx_route2cross1][-exch_len - 1]
            else:
                sol_1_temp[idx_route2cross1][-exch_len:-exch_len] = nx.dijkstra_path(route, sol_1_temp[idx_route2cross1][-exch_len]-1, sol_1_temp[-exch_len])[1:-1]
        if exch_len < len(sol_2_temp[idx_route2cross2]):
            if sol_2_temp[idx_route2cross2][exch_len] not in list(route.neighbors(sol_2_temp[idx_route2cross2][exch_len - 1])):
                if sol_2_temp[idx_route2cross2][exch_len] == sol_2_temp[idx_route2cross2][exch_len-1]:
                    del sol_2_temp[idx_route2cross2][exch_len]
                else:
                    sol_2_temp[idx_route2cross2][exch_len:exch_len] = nx.dijkstra_path(route, sol_2_temp[idx_route2cross2][exch_len-1], sol_2_temp[idx_route2cross2][exch_len])[1:-1]
    elif exch_len == len(sol_1_temp[idx_route2cross1]) :
        if exch_len < len(sol_2_temp[idx_route2cross2]):
            if sol_2_temp[idx_route2cross2][exch_len] not in list(route.neighbors(sol_1_temp[idx_route2cross1][exch_len - 1])):
                if sol_2_temp[idx_route2cross2][exch_len] == sol_2_temp[idx_route2cross2][exch_len-1]:
                    del sol_2_temp[idx_route2cross2][exch_len]
                else:
                    sol_2_temp[idx_route2cross2][exch_len:exch_len] = nx.dijkstra_path(route, sol_2_temp[idx_route2cross2][exch_len-1], sol_2_temp[idx_route2cross2][exch_len])[1:-1]
    if len(sol_1_temp[idx_route2cross1]) == 1:
        temp_neighbors = list(route.neighbors(sol_1_temp[idx_route2cross1][0]))
        actual_node = temp_neighbors[np.random.randint(0, len(temp_neighbors))]
        sol_1_temp[idx_route2cross1].append(actual_node)
    if len(sol_2_temp[idx_route2cross2]) == 1:
        temp_neighbors = list(route.neighbors(sol_2_temp[idx_route2cross2][0]))
        actual_node = temp_neighbors[np.random.randint(0, len(temp_neighbors))]
        sol_2_temp[idx_route2cross2].append(actual_node)
    return [sol_1_temp, sol_2_temp]