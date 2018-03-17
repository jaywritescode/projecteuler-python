class Graph:

    def __init__(self):
        self.nodes = dict()

    def add_node(self, node):
        """
        Add a node to this graph. All nodes in the graph must have unique labels.

        Args:
            node: The node to add.

        Returns:
            The node.
        """
        if node.label not in self.nodes:
            self.nodes[node.label] = node
        return node
