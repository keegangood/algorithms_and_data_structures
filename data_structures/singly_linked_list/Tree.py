class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        root = None

    def preorder(self):
        pass

    def postorder(self):
        pass

    def inorder(self):
        pass



if __name__ == '__main__':
    t = Tree()
    t.root = TreeNode(10)

    t.root.left = TreeNode(2) 
    t.root.right = TreeNode(3) 
    t.root.left.left = TreeNode(4) 
    t.root.left.right = TreeNode(5) 


    t.inorder()