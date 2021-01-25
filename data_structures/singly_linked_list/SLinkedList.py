class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val 

class SLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return '-> '.join(nodes)


if __name__ == '__main__':
    import random

    s = SLinkedList()

    for i in range(10):
        if not s.head:
            s.head = Node(i)
            curr = s.head

        else:
            n = Node(i)
            curr.next = n 

            curr = n        

        
        
    print(s) 
    # 0-> 1-> 2-> 3-> 4-> 5-> 6-> 7-> 8-> 9