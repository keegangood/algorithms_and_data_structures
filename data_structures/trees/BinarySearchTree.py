class BSTNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.right = None
        self.left = None
        self.count = 1

    def __repr__(self):
        return str(self.val)

class BST:
    def __init__(self):
        self.root = None
    
    def _search(self, number, root):
        if root is None:
            return False

        if number == root.val:
            return root
        
        elif number > root.val:
            return self._search(number, root.right)

        elif number < root.val:
            return self._search(number, root.left)
        
    def search(self, number):
        return self._search(number, self.root)

    def _insert(self, val, root):
        '''recursively place the new value'''
        if root is None:
            node = BSTNode(val)
            if self.root is None:
                self.root = node
            return node
        
        # if the value is equal to the root
        if val == root.val:
            root.count += 1
            return root

        # if the value is less than the root's value
        elif val < root.val:
            # if left node is empty
            if root.left is None:
                root.left = BSTNode(val)
                return root.left

            else:
                # call _insert() on left child
                self._insert(val, root.left)

        elif val > root.val:
            if root.right is None:
                root.right = BSTNode(val)
                return root.right
            else:
                # call _insert() on return child
                self._insert(val, root.right)

    def insert(self, val):
        return self._insert(val, self.root)
        
    def delete(self, val):
        pass
    
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
    from random import randint

    bst = BST()

    nums = [randint(1, 10) for i in range(10)]

    for num in nums:
        bst.insert(num)

    val = 5
    node = bst.search(val)
    if node:
        print(f'The value {val} exists in the BST {node.count} times')
    else:
        print(f'The value {val} does not exist in the BST')


