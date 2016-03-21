"""
File: counter.py
Author: Ken Lambert
Name: Leigh Stauffer
Project 6
"""

class Counter(object):
    """Represents a counter object."""

    def __init__(self):
        self._number = 0

    def increment(self, amount = 1):
        self._number += amount

    def __str__(self):
        return str(self._number)

    def reset(self):
        self._number = 0
