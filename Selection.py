from obj_fun import obj_fun
from typing import List
from operator import itemgetter
import numpy as np

import networkx as nx

''' ZWYKLA NAJLEPSZE
def selection(population: List, dest_mat, route_graph, parents_div=5):
    obj_fun_dict = {}
    for elem in range(len(population)):
        obj_fun_dict[elem]=obj_fun(population[elem], dest_mat, route_graph)

    sorted_obj_fun_dict = sorted(obj_fun_dict.items(), key=itemgetter(1))  #sortowanie po wartości słownika

    parents_list = []
    for i in range(len(sorted_obj_fun_dict)//parents_div):
        parents_list.append(population[sorted_obj_fun_dict[-(i+1)][0]])
    return parents_list
'''
 #zwracanie najleposzego
def selection_best_end(population: List, dest_mat, route_graph: nx.Graph):
    obj_fun_dict = {}
    for elem in range(len(population)):
        obj_fun_dict[elem] = obj_fun(population[elem], dest_mat, route_graph)

    sorted_obj_fun_dict = sorted(obj_fun_dict.items(), key=itemgetter(1))  #sortowanie po wartości słownika
    return [population[sorted_obj_fun_dict[-1][0]], sorted_obj_fun_dict[-1][1]]


# ta jest dobra zwykla
def selection_basic(population: List, dest_mat, route_graph, parents_div=5):
    obj_fun_dict = {}
    for elem in range(len(population)):
        obj_fun_dict[elem] = obj_fun(population[elem], dest_mat, route_graph)

    sorted_obj_fun_dict = sorted(obj_fun_dict.items(), key=itemgetter(1))  #sortowanie po wartości słownika

    parents_list = []
    for i in range(len(sorted_obj_fun_dict)//parents_div):
        parents_list.append(population[sorted_obj_fun_dict[-(i+1)][0]])
    return parents_list


# selekcja rankingowa liniowa plus ruletka


def selection(population: List, dest_mat, route_graph, linear_coef=1.5, parents_div=2):
    obj_fun_dict = {}
    for elem in range(len(population)):
        obj_fun_dict[elem]=obj_fun(population[elem], dest_mat, route_graph)

    sorted_obj_fun_dict = sorted(obj_fun_dict.items(), key=itemgetter(1))  #sortowanie po wartości słownika

    parents_list = []
    probability_list = []

    lambda_c = len(sorted_obj_fun_dict)
    eta_max = linear_coef
    eta_min = 2-linear_coef
    for idx, elem in enumerate(sorted_obj_fun_dict):
        probability_list.append((1/lambda_c)*(eta_max-(eta_max-eta_min)*idx/(lambda_c-1)))
    probability_list.reverse()

    probability_list_sum = []
    sum_prob = 0
    for elem in probability_list:
        probability_list_sum.append(sum_prob + elem)
        sum_prob += elem

    for i in range(len(sorted_obj_fun_dict)//parents_div):
        rand_prob = np.random.sample()
        filtered_roulette = (idx for idx, elem in enumerate(probability_list_sum) if elem > rand_prob)
        roulette_index = next(filtered_roulette)
        parents_list.append(population[sorted_obj_fun_dict[-(roulette_index+1)][0]])

    return parents_list
