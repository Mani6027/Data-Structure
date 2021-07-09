from collections import defaultdict, OrderedDict

class Graph:
  def __init__(self):
    self.data = defaultdict(list)
  
  def add_edge(self, node, edge, undirectional=True):
    self.data[node].append(edge)
    if undirectional:
      self.data[edge].append(node)
  
  def print_adj_list(self):
    for key, val in self.data.items():
      print(key, '-->', val)

g = Graph()
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(2,1)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(2,3)
g.add_edge(3,5)

g.print_adj_list()
