from . import graph

class AdjacencySetGraph(graph.Graph):

    class Node:
        def __init__(self, label, color=None):
            self.label = label
            self.color = color
            self.neighbors = dict()

        def add_neighbor(self, neighbor, cost=1):
            if neighbor not in self.neighbors:
                self.neighbors[neighbor] = cost

        def get_neighbors(self):
            """
            Gets this node's neighbors, without regard to the cost of the edge
            to each neighbor.

            Returns:
                A list of this node's neighbors.
            """
            return list(self.neighbors.keys())

        def __str__(self):
            return "{}{}".format(self.label, ': ({})'.format(self.color) if self.color else '')

    def __init__(self, is_directed=True):
        super(AdjacencySetGraph, self).__init__()
        self.is_directed = is_directed

    def add_node(self, label, color=None):
        """
        Creates a node with the given label and color and adds it to the graph.
        """
        node = AdjacencySetGraph.Node(label, color)
        return super(AdjacencySetGraph, self).add_node(node)

    def add_edge(self, node_source, node_sink, cost=1):
        """
        Creates an edge from node_source to node_sink.

        Args:
            node_source: The starting node for the edge.
            node_sink: The terminating node for the edge.
            cost: The edge cost, for weighted graphs.

        Returns:
            None.
        """
        node_source.add_neighbor(node_sink, cost)
        if not self.is_directed:
            node_sink.add_neighbor(node_source, cost)

    def __str__(self):
        return "\n".join(
            "{} --> {}".format(
                str(node),
                ', '.join(str(neighbor.label) for neighbor in node.get_neighbors())
            ) for node in self.nodes)
