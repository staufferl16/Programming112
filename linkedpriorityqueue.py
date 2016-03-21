"""
File: linkedpriorityqueue.py
Author: Leigh Stauffer
Project 7
"""

from node import Node
from linkedqueue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queue implementation."""


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, item):
        """Adds item to its proper place in the queue."""
        if self.isEmpty() or item >= self._rear.data:
            LinkedQueue.add(self, item)
        elif item < self._front.data:
            self._front = Node(item, self._front)
            self._size += 1
        else:
            probe = self._front
            trailer = probe
            while item >= data:
                trailer = probe
                probe = probe.next
            trailer.next = Node(item, probe)
