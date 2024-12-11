
class BST_Node:
    """Class to represent a single node in a BST"""
    def __init__(self, key, value):
        self.key = key      # uniquely identifies the node.
        self.value = value  #data associated with the key
        self.left = None    #Node initiated with no left child (no left subtree)
        self.right = None   #Node initiated with no right child (no right subtree)

class Binary_Search_Tree:
    """BST Class to represent each bucket in the hash table"""
    def __init__(self):
        """initialises the tree with empty node"""
        self.root = None

    def insert(self, key, value):
        """Inserts a new key-value pair into the BST"""
        def _insert(node, key, value):
            """helper function to recursively find the correct position for the key"""
            if not node: #empty tree(or subtree)
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
            if not node: # empty tree (or subtree)
                return None
            if key == node.key:
                return node.value
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key) #returns search results

    def delete(self, key):
        """Deletes the key-value pair from the BST and maintains the BST structure"""
        def _delete(node, key):
            """helper function to recursively locate and delete the node"""
            if not node: #empty tree (or subtree)
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node to delete is found: key matches the current node's key
                if not node.left:  #Node found with no left child
                    return node.right  #returns right child (or None if it has no right child)
                elif not node.right: #Node found with no right child
                    return node.left  #returns left child (or None if it has no left child)

                # Node with two children:
                successor = self._find_min(node.right) #gets the inorder successor
                node.key, node.value = successor.key, successor.value
                node.right = _delete(node.right, successor.key)
            return node #return the updated node to rebuild the tree structure

        self.root = _delete(self.root, key) #updates the root after deletion

    def _find_min(self, node):
        """Finds the smallest key in a given subtree"""
        while node.left:
            node = node.left
        return node

    def is_empty(self):
        """Checks if the tree is empty"""
        return self.root is None
    
class Hybrid_DS:
    """Class for the hybrid data structure"""
    def __init__(self, table_size):
        """class Hybrid_DS initialised with hash table of fixed size and empty buckets (arrays)"""
        self.table_size = table_size
        self.table = [None] * table_size #each bucket will hold a BST