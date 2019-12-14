# funkcja celu
import numpy as np
import networkx as nx

from typing import List
from copy import deepcopy

#zmienna globalna zliczajaca ilosc iteracji f celu
num_of_obj = 0

'''
def obj_fun(curr_pop: List, dest_mat):
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
'''


def obj_fun(solution: List, dest_mat, route: nx.Graph,  ticket_cost=5, fuel_cost=2, start_cost=10):
    const_cost = 1
    temp_dest_fun = 0
    sol_cost = 0
    num_of_passengers = 0
    route_weight = 0
    dest_mat_temp = deepcopy(dest_mat)
    for bus in solution:
        #print('bus',bus)
        sol_cost = sol_cost - start_cost      #koszt uruchomienia autobusu
        bus_stop_combinations = []      #wszystkie kombinacje przystankow source->destination
        for b_stop in range(len(bus)-1):
            route_weight += route.get_edge_data(bus[b_stop], bus[b_stop+1])['weight']   #suma wag krawedzi tworzacej trasy

            #print([bus[b_stop], bus[b_stop+1]])
            #print(route.get_edge_data(bus[b_stop], bus[b_stop+1])['weight'])
            for comb in range(len(bus)-1-b_stop):
                bus_stop_combinations.append([bus[b_stop], bus[comb]])
        for combination in bus_stop_combinations:
            num_of_passengers += dest_mat_temp[combination[0]-1][combination[1]-1]
            dest_mat_temp[combination[0]-1][combination[1]-1] = 0
    sol_cost += num_of_passengers * ticket_cost     # dochod bilety
    sol_cost = sol_cost - route_weight*fuel_cost
    global num_of_obj
    num_of_obj += 1
    return sol_cost
