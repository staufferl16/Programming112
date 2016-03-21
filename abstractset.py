"""
Author:  Leigh Stauffer
Project 5
File Name: abstractset.py
"""

class AbstractSet(object):
    """"""

    def __or__(self, other):
        """Returns a set containing all the items in s1 and s2."""
        return self + other

    def __and__(self, other):
        """Returns a set containing only the items in s1 that are also in s2."""
        tempCollection = type(self)()
        for item in self:
            if item in other:
               tempCollection.add(item)
        return tempCollection

    def __sub__(self, other):
        """Returns a set containing the only items in s1 that are not in s2."""
        tempCollection = type(self)()
        for item in self:
            if not item in other:
                tempCollection.add(item)
        return tempCollection
