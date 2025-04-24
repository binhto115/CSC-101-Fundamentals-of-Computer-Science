import unittest

from linked_list import Node, add, empty_list, get, length, remove, setitem, LinkedList


class Tests(unittest.TestCase):
    def test_length_empty_list(self) -> None:
        self.assertEqual(
            length(empty_list()),
            0,
        )

    def test_add_empty_list(self) -> None:
        # NOTE: You will need to define __eq__ in your Node class for
        # this test to pass.
        self.assertEqual(
            add(empty_list(), 0, "hello"),
            Node("hello", None),
        )
    def test_get_from_empty_list(self):
        with self.assertRaises(IndexError):
            get(None, 0)
    def test_get_empty_list(self) -> any:
        self.assertEqual(get(Node(10, Node(20, Node(30, None))), 2), 30)

    def test_get_list(self) -> any:
        self.assertEqual(get(Node(1, Node("Hello", Node(
            3, Node(4, Node(5, None))))), 1), "Hello")

    def test_setitem_list(self):
        node_list = Node(1, Node(4, Node(3, Node(4, None))))
        node_outcome = Node(1, Node(2, Node(3, Node(4, None))))
        self.assertEqual(setitem(node_list, 3, 2), node_outcome)

    def test_setitem_empty_list(self):
        with self.assertRaises(IndexError):
            setitem(None, 0, 104)
# TODO: Add more tests!


if __name__ == "__main__":
    unittest.main()
