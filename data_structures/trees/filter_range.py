from BinarySearchTree import BST, BSTNode

'''
Given a BST and a valid range of keys, remove nodes
from the BST that have keys outside that range.
'''


def truncate(root, low, high):
    if root is None:
        return root
    
    root.left = truncate(root.left, low, high)
    root.right = truncate(root.right, low, high)

    if root.val > high:
        root = root.left
    elif root.val < low:
        root = root.right

    return root

bst = BST()
keys = [15, 10, 20, 8, 12, 16, 25]

for key in keys:
    bst.insert(key)

bst.preorder(bst.root)
print()
truncate(bst.root, 9, 12)
bst.preorder(bst.root)
