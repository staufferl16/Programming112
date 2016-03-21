"""
Author: Leigh Stauffer
Project 5
File Name: linkedset.py
"""
from linkedbag import LinkedBag
from node import Node
from abstractset import AbstractSet

class LinkedSet(LinkedBag, AbstractSet):
    """A link-based set implementation."""

    #Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes
        the contents of sourceCollection, if it's present."""
        LinkedBag.__init__(self, sourceCollection)
        
    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    #Mutator method
    def add(self, item):
        """Adds item to self."""
        if not item in self:
            LinkedBag.add(self, item)
