from collections.abc import MutableSequence
from typing import Iterable, Any, Optional
from node import Node


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable):
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value):

        append_node = Node(value)
        if self._len == 0:
            self._head = self._tail = append_node
        else:
            self.link_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    @staticmethod
    def link_nodes(left_node, right_node):
        left_node.next = right_node

    def step_by_step_on_nodes(self, index: int) -> Node:

        if not isinstance(index, int):
            raise TypeError("Wrong index type")
        if not 0 <= index < self._len:
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def insert(self, index: int, value: Any) -> None:
        pass

    def __getitem__(self, index: int) -> Any:
        return self.step_by_step_on_nodes(index).value

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        if index == 0:
            self._head = self._head.next
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            current_node = prev_node.next
            if current_node == self._tail:
                self._tail = prev_node
            next_node = current_node.next
            self.link_nodes(prev_node, next_node)
        self._len -= 1

    def __len__(self) -> int:
        return self._len


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ...
