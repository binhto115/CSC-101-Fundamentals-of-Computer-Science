from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: LinkedList):
        self.value = value
        self.next = nxt

    def __eq__(self, other) -> bool:
        return (isinstance(other, Node) and
                self.value == other.value or
                self.next == other.next
                )

    def __repr__(self) -> str:
        return "Node(%r, %r)" % (self.value, self.next)


LinkedList = Optional[Node]


def empty_list() -> LinkedList:
    return None


def add(lst: LinkedList, index: int, value: Any) -> LinkedList:

    if lst is None:
        return 0
    else:
        pass


def length(lst: LinkedList) -> int:
    if lst is None:
        return 0
    else:
        return 1 + length(lst.next)


def get(lst: LinkedList, index: int) -> Any:
    lst_index = 0
    if index >= length(lst):
        raise IndexError
    elif lst is None:
        return 0
    elif lst_index != index:
        return get(lst.next, index-1)
    else:
        return lst.value


def setitem(lst: LinkedList, index: int, value: Any) -> LinkedList:
    temp = lst
    temp_2 = lst
    lst_index = 0
    if index >= length(lst):
        raise IndexError
    elif lst is None:
        raise IndexError
    elif lst_index != index:
        temp_2 = setitem(temp_2.next, index-1, value)
    else:
        lst.value = value
    return temp
print("da result " + str(setitem(Node(1, Node(3, Node(3, Node(4, None)))), 2, "Yes")))

def remove(lst: LinkedList, index: int) -> tuple[Any, LinkedList]:
    """Return a tuple of the removed element and a new list"""
    removed_element = 0
    temp_1 = lst
    temp_2 = lst  # Node(1, Node(2, Node(3, None)))
    lst_index = 0
    if index >= length(lst):
        raise IndexError
    elif lst is None:
        raise IndexError
    elif lst_index != index:
        remove(temp_2.next, index-1)
    else:
        removed_element = get(temp_2, 0)
        print(removed_element)
        if temp_2.value == removed_element:
            temp_2.value = 0
    print(removed_element)
    return tuple(removed_element, temp_1)
