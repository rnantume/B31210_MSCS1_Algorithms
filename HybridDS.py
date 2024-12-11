
class BST_Node:
    """Class to represent a single node in a BST"""
    def __init__(self, key, value):
        self.key = key      # uniquely identifies the node.
        self.value = value  #data associated with the key
        self.left = None    #Node initiated with no left child (no left subtree)
        self.right = None   #Node initiated with no right child (no right subtree)

class Binary_Search_Tree:
    """Class to represent the BST in each bucket"""
    def __init__(self):
        """initialises the tree with empty node"""
        self.root = None

    def insert(self, key, value):
        """Inserts a new key-value pair into the BST"""
        def _insert(node, key, value):
            """helper function to recursively find the correct position for the key"""
            if not node: #empty BST
                return BST_Node(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value  # Update value if key exists
            return node

        self.root = _insert(self.root, key, value) #Updates the root after the insertion

    def search(self, key):
        """Searches for a key in the BST and returns its value if found; else returns None"""
        def _search(node, key):
            """helper function to recursively traverse the BST"""
            if not node: # empty BST
                return None
            if key == node.key:
                return node.value
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

