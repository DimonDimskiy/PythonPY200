from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_




class DoubleLinkedNode(Node):

    def __init__(self, value: Any, next_: Optional["DoubleLinkedNode"] = None,
                 previous: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.previous = previous

    def __repr__(self):

        return f"{self.__class__.__name__}({self.value}, {self.next}, {self.previous})"

    def is_valid(self, dlnode: Any) -> None:
        if not isinstance(dlnode, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, previous: Optional["DoubleLinkedNode"]):
        self.is_valid(previous)
        self._previous = previous



