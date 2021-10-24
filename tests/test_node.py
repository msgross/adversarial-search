""" Tests for our Node class and DummyNode class
    Make sure we can build a tree sufficiently and search through it

"""

from unittest import TestCase
from node import Node
from node import DummyNode


class TestNode(TestCase):
    """ Node test class

    """
    def test_dummy_node(self):
        """ Test our dummy node to make sure that if no data is wanted to be retained
            dummy node throws everything out

        :return: success if DummyNode does nothing useful
        """
        node = DummyNode("root")
        child_node = node.add_child("child")
        self.assertTrue(node.is_leaf())
        self.assertListEqual(node.get_children(), [], "Make sure no children are added to dummy node")
        self.assertIsNone(node.find("child"), "Make sure we don't find children in here")
        self.assertIsNone(node.get_value(), "Make sure we don't retain value in this node")
        self.assertIsNone(child_node.get_value(), "Make sure created child has no value")

    def test_node(self):
        """ Test our node to make sure that child and grandchild values can be found

        :return: success if we can build a simple tree from a starting node
        """
        node = Node("root")
        child_node = node.add_child("child")
        self.assertFalse(node.is_leaf(), "Make sure this node is not a leaf")
        self.assertTrue(child_node.is_leaf(), "New child should be a leaf")
        self.assertEqual(node.find("child").get_value(), "child", "Find child node successfully")
        self.assertEqual(len(node.get_children()), 1, "Should be one child")
        child_node.add_child("grandchild")
        self.assertEqual(len(node.get_children()), 1, "Should still only be one child")
        self.assertEqual(node.find("grandchild").get_value(), "grandchild", "Find grandchild node successfully")

