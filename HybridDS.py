
class BSTNode:
    """class for data structure to represent a single node in a BST"""
    def __init__(self, key, value):
        self.key = key      # uniquely identifies the node.
        self.value = value  #data associated with the key
        self.left = None    #left child set to none to indicate note has no children at initiation
        self.right = None   #left child set to none to indicate note has no children at initiation
