"""
File: node.py
Editor: Leigh Stauffer
Project 11

One-way nodes for linked structures.

To instantiate, use

<variable> = Node(<dataum>, <optional next node>)

The next node is None by default.
"""

class Node(object):

   def __init__(self, data, next = None):
       self.data = data
       self.next = next
