from SLinkedList import SLinkedList, Node

s = SLinkedList()

s.head = Node(1)

n = s.head
for i in range(10):
    n.next = Node(i)
    if i == 6:
        loop_node = n
    n = n.next

n.next = loop_node

print(s)