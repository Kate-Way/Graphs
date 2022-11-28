# Undirected unweighted graph using adjacency list

class Graph:
    def __init__(self):
        self.nodes_count = 0
        self.nodes_list = {}

    def add_vertex(self, val):
        if val not in self.nodes_list:
            self.nodes_list[val] = []
            self.nodes_count += 1
        else:
            raise "Already in the list"

    def add_edge(self, val1, val2):
        if val1 in self.nodes_list and val2 in self.nodes_list:
            self.nodes_list[val1].append(val2)
            self.nodes_list[val2].append(val1)
        elif val1 not in self.nodes_list:
            raise f"{val1} not in the list"
        else:
            raise f"{val2} not in the list"

    def print(self):
        print(self.nodes_list)


# Test

# graph = Graph()
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)
# graph.add_vertex(4)
# graph.add_edge(2,3)
# graph.add_edge(1,3)
# graph.add_edge(2,4)
# graph.print()



