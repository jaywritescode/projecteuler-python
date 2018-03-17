from project.graphs.adjacency_set_graph import *
import unittest

class TestAdjacencySetGraph(unittest.TestCase):

    def test_init(self):
        graph = AdjacencySetGraph()
        self.assertEqual(len(graph.nodes), 0)

    def test_add_node(self):
        graph = AdjacencySetGraph()

        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)

        self.assertEqual(len(graph.nodes), 3)

    def test_add_edge(self):
        graph = AdjacencySetGraph(is_directed=True)

        node1 = graph.add_node(1)
        node2 = graph.add_node(2)
        node3 = graph.add_node(3)

        edge12 = graph.add_edge(node1, node2)
        edge21 = graph.add_edge(node2, node1)
        edge13 = graph.add_edge(node1, node3)

        self.assertEqual(set(node1.neighbors.keys()), set([node2, node3]))
        self.assertEqual(set(node2.neighbors.keys()), set([node1]))
        self.assertEqual(set(node3.neighbors.keys()), set())
