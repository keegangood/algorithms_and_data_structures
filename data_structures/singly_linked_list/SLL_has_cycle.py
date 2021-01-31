from SLinkedList import SLinkedList, Node

def has_cycle(head):
    slow = head
    fast = head.next

    # while pointers aren't None
    while slow and fast:

        # if the slow and fast pointers land 
        # on the same node, a cycle exists
        if slow == fast:
            return True
        
        # progress the slow pointer
        slow = slow.next
        
        # if fast
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            return False

# -------------------------------------------------- #
s = SLinkedList()

s.head = Node(1)

n = s.head
for i in range(10):
    n.next = Node(i)
    # save node to create cycle
    if i == 3:
        loop_node = n
    n = n.next

# cycle last node back in list
n.next = loop_node

print(has_cycle(s.head))

# -------------------------------------------- #
s2 = SLinkedList()

s2.head = Node(0)
n = s2.head
for i in range(1,11):
    n.next = Node(i)
    n = n.next

print(has_cycle(s2.head))