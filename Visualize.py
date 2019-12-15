import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from typing import List
from copy import deepcopy


def visualize_best_route(route: nx.Graph, best_sol: List):
    '''
    colors = range(3)
    options = {

        "with_labels": True,
    }
    nx.draw(route,**options )
    plt.show()

    pos = nx.spring_layout(route)
    nodes = nx.draw_networkx_nodes(route, pos, node_size=800)
    edges = nx.draw_networkx_edges(
        route,
        pos,
        edge_color=(0.1, 0.3, 0.7),
        width=3
    )
    edges = [(1,2),(2,3)]
    directed_sol = nx.DiGraph()
    directed_sol.add_edges_from(edges)
    pos1 = nx.spring_layout(directed_sol)
    nodes1 = nx.draw_networkx_nodes(directed_sol, pos, node_size=3)
    edges1 = nx.draw_networkx_edges(
        directed_sol,
        pos,
        arrowsize=20,
        arrowstyle='->'
    )
    nx.draw_networkx_labels(route, pos, font_size=20)
    plt.show()'''

    pos = nx.circular_layout(route)

    #nodes_basic = nx.draw_networkx_nodes(route, pos, node_size=600)
    #edges_basic = nx.draw_networkx_edges(
     #   route,
      #  pos,
       # width=1
    #)
    #nx.draw_networkx_labels(route, pos, font_size=10)

    bus_lines_edges = []
    for bus in best_sol[0]:
        bus_line_edges = []
        for b_stop in range(len(bus)-1):
            bus_line_edges.append((bus[b_stop], bus[b_stop+1]))
        bus_lines_edges.append(deepcopy(bus_line_edges))
    directed_graph_lines = []
    for line in bus_lines_edges:



        directed_graph_lines.append(nx.DiGraph())
        directed_graph_lines[-1].add_edges_from(line)

    if len(directed_graph_lines)>1:
        fig, ax = plt.subplots(len(directed_graph_lines))

        for idx, line_graph in enumerate(directed_graph_lines):
            nx.draw_networkx_nodes(route, pos, node_size=600, ax=ax[idx])
            nx.draw_networkx_edges(
                route,
                pos,
                ax=ax[idx],
                width=1
              )
            nx.draw_networkx_labels(route, pos, font_size=10, ax=ax[idx])
            nx.draw_networkx_edges(
                line_graph,
                pos,
                edge_color='r',
                arrowsize=15,
                width=2,
                ax=ax[idx]

            )
            ax[idx].set_title('Linia numer {}'.format(idx+1), fontsize=10)
    else:
        nx.draw_networkx_nodes(route, pos, node_size=600,)
        nx.draw_networkx_edges(
            route,
            pos,
            width=1
        )
        nx.draw_networkx_labels(route, pos, font_size=10)
        nx.draw_networkx_edges(
            directed_graph_lines[0],
            pos,
            edge_color='r',
            arrowsize=15,
            width=2,

        )
        plt.title('Linia numer {}'.format(1), fontsize=10)

    plt.show()
