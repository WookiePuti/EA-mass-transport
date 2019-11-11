# funkcja celu
import numpy as np
import networkx as nx

def obj_fun(curr_pop: np.array, dest_mat):
    ticket_cost = 5
    const_cost = 1
    fuel_cost = 2
    temp_dest_fun = 0
    for num_of_bus in range(len(curr_pop)):
        temp_dest_fun += temp_dest_fun
        for x in range(len(curr_pop[num_of_bus])-1):
            if curr_pop[num_of_bus][x+1] != curr_pop[num_of_bus][x]:
                temp_dest_fun+=dest_mat[curr_pop[num_of_bus][x]][curr_pop[num_of_bus][x+1]]*ticket_cost-const_cost
    return temp_dest_fun
