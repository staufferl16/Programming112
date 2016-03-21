"""
Name: Leigh Stauffer
Project 6
File: linkedstack.py
Author: Ken Lambert
"""

from abstractstack import AbstractStack
from node import Node

class LinkedStack(AbstractStack):
    """Represents a link-based stack."""

    def __init__(self, sourceCollection = None):
        self._head = None
        AbstractStack.__init__(self, sourceCollection)

    def push(self, item):
        self._head = Node(item, self._head)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise ValueError("Attempt to pop from empty stack")
        self._size -= 1
        data = self._head.data
        self._head = self._head.next
        return data

    def peek(self):
        if self.isEmpty():
            raise ValueError("Attempt to peek at empty stack")
        return self._head.data

    def __iter__(self):
        lyst = list()
        probe = self._head
        while probe != None:
            lyst.append(probe.data)
            probe = probe.next
        lyst.reverse()
        return iter(lyst)

def test():
    """Tests a linked stack."""
    stack = LinkedStack(range(5))
    print("Expect [0, 1, 2, 3, 4]: ", stack)
    print("Expect 4 3 2 1 0: ", end="")
    while not stack.isEmpty():
        print(stack.pop(), end = " ")

if __name__ == '__main__': 
    test()
