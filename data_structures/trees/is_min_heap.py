from Tree import Tree, TreeNode

def is_min_heap(root):
    if root is None:
        return True

    if (root.right and root.val >= root.right.val) or \
        (root.left and root.val >= root.left.val):
        return False

    return is_min_heap(root.left) and is_min_heap(root.right)

if __name__ == '__main__':
    t = Tree()

    t.root = TreeNode(2)
    t.root.left = TreeNode(3)
    t.root.right = TreeNode(4)
    t.root.left.left = TreeNode(5)
    t.root.left.right = TreeNode(6)
    t.root.right.left = TreeNode(8)
    t.root.right.right = TreeNode(10)

    print(is_min_heap(t.root))