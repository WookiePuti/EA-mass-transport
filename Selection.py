from obj_fun import obj_fun
from typing import List
from operator import itemgetter


def selection(population: List, dest_mat, route_graph, parents_div=5):
    obj_fun_dict = {}
    for elem in range(len(population)):
        obj_fun_dict[elem]=obj_fun(population[elem], dest_mat, route_graph)

    sorted_obj_fun_dict = sorted(obj_fun_dict.items(), key=itemgetter(1))  #sortowanie po wartości słownika

    parents_list = []
    for i in range(len(sorted_obj_fun_dict)//parents_div):
        parents_list.append(population[sorted_obj_fun_dict[-(i+1)][0]])
    return parents_list