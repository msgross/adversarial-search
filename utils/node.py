""" Node class, can be assembled into a tree

"""


class Node:
    """ A node in a tree

    """
    def __init__(self, value):
        """ Constructor

        :param value: value that will be wrapped in a node as a child of this node
        """
        self.value = value
        self.children = []

    def add_child(self, node_value):
        """ Add a new node as a child of this node

        :param node_value: the node value to be wrapped in a node and added as
                            a child of this node
        :return: the newly created node
        """
        new_node = Node(node_value)
        self.children.append(new_node)
        return new_node

    def is_leaf(self) -> bool:
        """ Method returns true if this node is a leaf

        :return: True if this node has no children, False otherwise
        """
        return len(self.children) == 0

    def find(self, val):
        """ Method searches for a given value within this node and its children

        :param val: the value being searched for
        :return: the node containing the value
        """
        if self.value is val:
            return self
        for child in self.children:
            found = child.find(val)
            if found is not None:
                return found
        return None

    def get_children(self):
        """ Getter for children list

        :return: the list of children for this node
        """
        return self.children

    def get_value(self):
        """ Getter for value

        :return: the value of this node
        """
        return self.value


class DummyNode(Node):
    """ A dummy node for a tree--these nodes are essentially dead-ends
        and are meant to provide something to pass that does nothing
        when holding on to that memory is unneeded

    """
    def __init__(self, value):
        """ Dummy Node, don't retain a value provided

        :param value: ignore
        """
        super.__init__(value)
        self.value = None

    def add_child(self, node_value):
        """ Dummy Node, don't add child

        :param node_value: ignore
        :return: a dummy node
        """
        return DummyNode(None)

    def is_leaf(self) -> bool:
        """ Always return true, no children

        :return: True
        """
        return True

    def find(self, val):
        """ Don't bother searching

        :param val: search parameter
        :return: None
        """
        return None

    def get_children(self):
        """ Return an empty list

        :return: empty list
        """
        return []

    def get_value(self):
        """ Getter for  dummy value

        :return: None
        """
        return None
