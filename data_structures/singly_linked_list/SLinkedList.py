class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        nodes = []
        curr = self.head

        while curr != None:
            nodes.append(str(curr.val))
            curr = curr.next

        return '-> '.join(nodes)


if __name__ == '__main__':
    import random

    s = SLinkedList()
    s.head = Node(1)
    # print(s)
    
    # for i in range(10):
        # n = Node(i)
        # curr.next = n
        # curr = n



    # print(s)
    # 0-> 1-> 2-> 3-> 4-> 5-> 6-> 7-> 8-> 9