# symulacja algorytmu
from typing import List, Any

import numpy as np
import networkx as nx

from obj_fun import obj_fun
from Selection import selection, selection_best_end, selection_basic
from Crossover_operator import crossover_oper
from Mutation import mutate1, mutate2

from copy import deepcopy
import obj_fun

best_parent_stats = []

#tworzenie losowego rozwiazania

def create_rand_sol(route: nx.Graph, max_num_of_bus=5, min_route_length=2):
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


def simulate_EA(route, start_pop_size, dest_mat, mutate_prob, num_obj_iter, linear_coef=1.5, parents_div=2,
                ticket_cost=5, fuel_cost=2, start_cost=10):
    parents = create_first_pop(route, start_pop_size)
    while obj_fun.num_of_obj < num_obj_iter:
        counter = 0
        parents = selection(parents, dest_mat, route, linear_coef, parents_div,
                                  ticket_cost, fuel_cost, start_cost)
        global best_parent_stats
        best_parent_stats.append(obj_fun.obj_fun(selection_best_end(parents, dest_mat, route, ticket_cost, fuel_cost, start_cost)[0],
                                                 dest_mat, route, ticket_cost, fuel_cost, start_cost))

        children = []
        while counter < start_pop_size:
            operation_kind = np.random.rand()
            if operation_kind < mutate_prob:
                children.append(mutate1(parents[np.random.randint(len(parents))], route))
                counter += 1
            elif operation_kind >= mutate_prob and counter < start_pop_size-1:
                crossed_temp_sol = []
                crossed_temp_sol = crossover_oper(parents[np.random.randint(len(parents))], parents[np.random.randint(len(parents))], route)

                for sol in crossed_temp_sol:
                    children.append(sol)
                counter += 2
        parents = children
        best_parent_stats.append(
            obj_fun.obj_fun(selection_best_end(parents, dest_mat, route, ticket_cost, fuel_cost, start_cost)[0],
                            dest_mat, route, ticket_cost, fuel_cost, start_cost))
    return selection_best_end(parents, dest_mat, route, ticket_cost, fuel_cost, start_cost)
