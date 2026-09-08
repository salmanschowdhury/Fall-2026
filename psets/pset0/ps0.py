#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v is None:
        return 0
    v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 2t+1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t-1 (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    while v.size > 2*t-1:
        if v.left is not None:
            left_size = v.left.size
        else:
            left_size = 0
        if v.right is not None:
            right_size = v.right.size
        else:
            right_size = 0
        if left_size >= right_size:
            v = v.left
        else:
            v = v.right
    return v
  
