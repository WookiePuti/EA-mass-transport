import numpy as np
import networkx as nx

from typing import List
from copy import deepcopy

#zamieniam w jednej trasie 1 losowo wybrany wierzcholek

'''
def mutate1(solution: List, route: nx.Graph):
    route_idx = np.random.randint(len(solution))
    bus_stop_idx = np.random.randint(len(solution[route_idx]))
    if bus_stop_idx == 0:
        temp_neighbors = list(route.neighbors(solution[route_idx][bus_stop_idx + 1]))
        solution[route_idx][0] = temp_neighbors[np.random.randint(len(temp_neighbors))]
    elif bus_stop_idx == len(solution[route_idx])-1:
        temp_neighbors = list(route.neighbors(solution[route_idx][bus_stop_idx - 1]))
        solution[route_idx][bus_stop_idx] = temp_neighbors[np.random.randint(len(temp_neighbors))]
    else:
        temp_neighbors = list(route.neighbors(solution[route_idx][bus_stop_idx - 1]))
        solution[route_idx][bus_stop_idx] = temp_neighbors[np.random.randint(len(temp_neighbors))]
        solution[route_idx][(bus_stop_idx+1):(bus_stop_idx+1)] = nx.dijkstra_path(route, solution[route_idx][bus_stop_idx], solution[route_idx][bus_stop_idx + 1])[1:-1]

'''

def mutate1(solution: List, route: nx.Graph):
    route_idx = np.random.randint(len(solution))
    bus_stop_idx = np.random.randint(len(solution[route_idx]))

    child = deepcopy(solution)
    if bus_stop_idx == 0:
        temp_neighbors = list(route.neighbors(child[route_idx][1]))
        temp_neighbors.remove(child[route_idx][0])
        child[route_idx][0] = temp_neighbors[np.random.randint(len(temp_neighbors))]
    elif bus_stop_idx == len(child[route_idx])-1:
        temp_neighbors = list(route.neighbors(child[route_idx][bus_stop_idx - 1]))
        temp_neighbors.remove(child[route_idx][bus_stop_idx])
        child[route_idx][bus_stop_idx] = temp_neighbors[np.random.randint(len(temp_neighbors))]
    else:
        temp_neighbors = list(route.neighbors(child[route_idx][bus_stop_idx - 1]))
        if child[route_idx][bus_stop_idx] in temp_neighbors:
            temp_neighbors.remove(child[route_idx][bus_stop_idx])
        if child[route_idx][bus_stop_idx+1] in temp_neighbors:
            temp_neighbors.remove(child[route_idx][bus_stop_idx+1])
        if temp_neighbors:
            child[route_idx][bus_stop_idx] = temp_neighbors[np.random.randint(len(temp_neighbors))]
            if child[route_idx][bus_stop_idx+1] not in list(route.neighbors(child[route_idx][bus_stop_idx])):
                child[route_idx][(bus_stop_idx+1):(bus_stop_idx+1)] = nx.dijkstra_path(route, child[route_idx][bus_stop_idx], child[route_idx][bus_stop_idx + 1])[1:-1]
    return child


# kryzuje elementy tras z innymi


def mutate2():
    pass

'''
def mutate1(solution: List, route: nx.Graph):
    route_idx = np.random.randint(len(solution))
    bus_stop_idx = np.random.randint(len(solution[route_idx]))
    print(route_idx)
    print(bus_stop_idx)
    if bus_stop_idx == 0:
        temp_neighbors = list(route.neighbors(solution[route_idx][1]))
        solution[route_idx][0] = temp_neighbors[np.random.randint(len(temp_neighbors))]
    elif bus_stop_idx == len(solution[route_idx])-1:
        temp_neighbors = list(route.neighbors(solution[route_idx][bus_stop_idx - 1]))
        solution[route_idx][bus_stop_idx] = temp_neighbors[np.random.randint(len(temp_neighbors))]
    else:
        temp_neighbors = list(route.neighbors(solution[route_idx][bus_stop_idx - 1]))
        solution[route_idx][bus_stop_idx] = temp_neighbors[np.random.randint(len(temp_neighbors))]
        solution[route_idx][(bus_stop_idx+1):(bus_stop_idx+1)] = nx.dijkstra_path(route, solution[route_idx][bus_stop_idx], solution[route_idx][bus_stop_idx + 1])[1:-1]
        '''