#!/usr/bin/python3
"""Creates a clase Node"""


class Node:
    """template for a node in a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes a new node
        Args:
            data(int): data of new node
            next_node: next node (Node)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """setter/getter of private instance attribute data"""
        return self.__data

    @property
    def next_node(self):
        """setter/getter of private instance attribute next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""
    def __init__(self):
        """Initializes a single linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list
        Args:
            value: value of the new node
        """
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
