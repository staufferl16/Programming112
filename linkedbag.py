"""
Author: Leigh Stauffer
Project 4
File: linkedbag.py
"""

from node import Node
from abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._items = None

    def add(self, item):
        """Adds item to self."""
        self._items = Node(item, self._items)
        self._size += 1

    def count(self, item):
        """Expects an item as an argument and returns the number of instances
        of the item in the bag."""
        probe = self._items
        itemCount = 0
        while probe != None:
            if item == probe.data:
                itemCount += 1
            probe = probe.next
        return itemCount

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the one before it, if it exists
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        # Unhook the node to be deleted, either the first one or one
        # thereafter
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self._size -= 1
        
        
