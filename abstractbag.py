"""
Author: Leigh Stauffer
Project 5
File Name: abstractbag.py
"""
from abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):
    """An abstract collection implementation. Behaves as a bag-like object."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents of
        sourceCollection if it's present."""
        return AbstractCollection.__init__(self, sourceCollection)

    def __str__(self):
        """Returns the string representation of self."""
        return AbstractCollection.__str__(self)
    
    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
