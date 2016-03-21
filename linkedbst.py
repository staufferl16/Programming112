"""
File: linkedbst.py
Author: Leigh Stauffer
Project 9
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from math import log
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        return self.preorder()

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            treeStack = LinkedStack()
            treeStack.push(self._root)
            while not treeStack.isEmpty():
                node = treeStack.pop()
                yield node.data
                if node.right != None:
                    treeStack.push(node.right)
                if node.left != None:
                    treeStack.push(node.left)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        def recurse (node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        lyst = list()
        queue = LinkedQueue()
        def recurse():
            if not queue.isEmpty():
                node = queue.pop()
                lyst.append(node.data)
                if node.left:
                    queue.add(node.left)
                if node.right:
                    queue.add(node.right)
                recurse()

        if not self.isEmpty():
            queue.add(self._root)
            recurse()
        return iter(lyst)
            
    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position 
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal, 
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None
        
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
                
        # Return None if the item is absent
        if itemRemoved == None: return None
        
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            
        # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right
                
        # Case 3: The node has no right child
            else:
                newChild = currentNode.left
                
        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
            
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """Precondition: item == newItem.
        Raises: KeyError if item != newItem.
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        if item != newItem: raise KeyError("Items must be equal")
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node is None or node.left is None and node.right is None:
                return 0
            else:
                return 1 + max(recurse(node.left), recurse(node.right))

        return recurse(self._root)
            
    def isBalanced(self):
        """Returns True if the tree is balaned or False otherwise.
        t is balanced iff t.height() < 2 * log2(len(t) + 1) - 1."""
        return self.height() < 2 * log(len(self) + 1, 2) - 1

    def rebalance(self):
        """Rebalances the tree."""
        if not self.isBalanced():
            treeLyst = list(self.inorder())
            self.clear()
            def rebuild(left, right):
                """Adds items in treeLyst to make a balanced tree."""
                if left <= right:
                    mid = (left + right) // 2
                    self.add(treeLyst[mid])
                    rebuild (left, mid -1)
                    rebuild (mid + 1, right)

            rebuild(0, len(treeLyst) - 1)

def main():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nExpect True for A in tree: ", "A" in tree)

    print("\nString:\n" + str(tree))

    clone = LinkedBST(tree)
    print("\nClone:\n" + str(clone))
    
    print("Expect True for tree == clone: ", tree == clone)

    print("\nFor loop: ", end="")
    for item in tree:
        print(item, end=" ")

    print("\n\ninorder traversal: ", end="")
    for item in tree.inorder(): print(item, end = " ")
    
    print("\n\npreorder traversal: ", end="")
    for item in tree.preorder(): print(item, end = " ")
    
    print("\n\npostorder traversal: ", end="")
    for item in tree.postorder(): print(item, end = " ")
    
    print("\n\nlevelorder traversal: ", end="")
    for item in tree.levelorder(): print(item, end = " ")

    print("\n\nRemoving all items:", end = " ")
    for item in "ABCDEFG":
        print(tree.remove(item), end=" ")

    print("\n\nExpect 0: ", len(tree))

    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))

    
if __name__ == "__main__":
    main()


