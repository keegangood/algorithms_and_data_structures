class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        root = None

    def preorder(self, n):
        '''left -> root -> right'''
        if n is None:
            return

        self.preorder(n.left)

        print(n.val, end=' ')

        self.preorder(n.right)

    def postorder(self, n):
        '''right -> root -> left'''
        if n is None:
            return
        
        self.postorder(n.right)

        print(n.val, end=' ')

        self.postorder(n.left)

    def inorder(self, n):
        '''root -> left -> right'''
        if n is None:
            return
        
        print(n.val, end=' ')

        self.inorder(n.left)

        self.inorder(n.right)



if __name__ == '__main__':
    t = Tree()
    t.root = TreeNode(4)

    t.root.right = TreeNode(6) 
    t.root.right.left = TreeNode(5)
    t.root.right.right = TreeNode(7)

    t.root.left = TreeNode(2) 
    t.root.left.left = TreeNode(1) 
    t.root.left.right = TreeNode(3) 

    print('\nPre-Order')
    t.preorder(t.root)
    
    print('\nIn-Order')
    t.inorder(t.root)

    print('\nPost-Order')
    t.postorder(t.root)