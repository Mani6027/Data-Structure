from collections import defaultdict

class Graph:
  def __init__(self, nodes):
    self.data = {node: [] for node in nodes}

  def add_edge(self, vertex, edge, undirected=False):
    self.data[vertex].append(edge)
    if undirected:
      self.data[edge].append(vertex)
  
  def print_adj_list(self):
    for key, val in self.data.items():
      print(key, '-->', val)

nodes = ['delhi', 'london', 'new york', 'paris']
g = Graph(nodes)

# Here 'london' is not connected with any of the given vertices
g.add_edge('delhi', 'london')
g.add_edge('new york', 'london')
g.add_edge('delhi', 'paris')
g.add_edge('paris', 'new york')

g.print_adj_list()