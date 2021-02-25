from queue import PriorityQueue as Q
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for node in range(1,11):
    G.add_node(node)
    
Dict_heuristic = {1: 0, 2: 8, 3: 5, 4: 7, 5: 3, 6: 6, 7: 5, 8: 3, 9: 1, 10: 0} 

G.add_edge(1,2, weight = 6)
G.add_edge(1,6, weight = 3)
G.add_edge(2,4, weight = 2)
G.add_edge(2,3, weight = 3)
G.add_edge(3,4, weight = 1)
G.add_edge(3,5, weight = 5)
G.add_edge(4,5, weight = 8)
G.add_edge(5,9, weight = 5)
G.add_edge(5,10, weight = 5)
G.add_edge(6,7, weight = 1)
G.add_edge(6,8, weight = 7)
G.add_edge(7,9, weight = 3)
G.add_edge(8,9, weight = 2)
G.add_edge(9,10, weight = 3)

print(nx.info(G))
labels = nx.get_edge_attributes(G,'weight')

edge_weight = list(labels)
edges = list(G.edges)
graph_nodes = list(G.nodes)
print(Dict_heuristic)

nx.draw(G, with_labels=True, font_weight='bold') #help printing graph
plt.show()
