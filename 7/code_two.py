#!/usr/bin/env python3.9
import re
import numpy as np

def count_bags(to_color, nodes, edges, colors):
    bags = 0
    for edge in np.where(graph[:,to_color] > 0)[0]:
        for color in np.where(graph[edge,:] < 0)[0]:
            color_bags = graph[edge,to_color]
            bags += color_bags + color_bags * count_bags(color, nodes, edges, colors)
    return bags
    
nodes = []
edges = []

with open('in.txt', 'r') as fd:
    rule = re.compile(r" bags contain | bags?, | bags?.")
    for line in fd:
        # s = rule.split(line)
        bags = list(filter(lambda x: 'bags' not in x, rule.split(line)[:-1]))
        node = bags.pop(0)
        nodes.append(node)
        for edge in bags:
            edge_element = [node]
            edge_element.extend(edge.split(' ', 1))
            edges.append(edge_element)

# Build graph
nodes = dict(zip(nodes,range(len(nodes))))
graph = np.zeros((len(edges), len(nodes)), dtype=int)
for i, edge in enumerate(edges):
    node = nodes[edge[0]]
    if edge[1] != 'no':
        n = int(edge[1])
        to_node = nodes[edge[2]]
        graph[i, node] = n
        graph[i, to_node] = -n

colors = dict(map(lambda x: (x[1], x[0]), nodes.items()))

bags = count_bags(nodes['shiny gold'], nodes, edges, colors)

print(bags)

