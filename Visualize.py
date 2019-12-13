import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def visualize_best_route(route:nx.Graph):
    nx.draw(route)
    plt.show()
