"""
File: node.py
Author: Ken Lambert
Editor: Leigh Stauffer
Project 7
"""

class Node(object):
    """Nodes for singly linked structures."""

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
