"""
Author: Leigh Stauffer
Project 4
File: node.py
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
