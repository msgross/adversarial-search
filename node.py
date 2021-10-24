

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node_value):
        new_node = Node(node_value)
        self.children.append(new_node)
        return new_node

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def find(self, val):
        if self.value is val:
            return self
        for child in self.children:
            found = child.find(val)
            if found is not None:
                return found
        return None

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def debug_print(self):
        print(str(self.value) + ":")
        for child in self.children:
            print(str(child.get_value()) + "\t")
        print("\n")
        for child in self.children:
            child.debug_print()


class DummyNode(Node):
    def add_child(self, node_value):
        return DummyNode(None)

    def is_leaf(self) -> bool:
        return True

    def find(self, val):
        return None

    def get_children(self):
        return []

    def get_value(self):
        return None


