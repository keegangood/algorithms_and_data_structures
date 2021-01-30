from SLinkedList import SLinkedList, Node

def kth_to_last_element(l_list, k):
    p1 = p2 = l_list.head

    for i in range(k):
        if p2 is None:
            return None
        p2 = p2.next
    
    while p2:
        p1 = p1.next
        p2 = p2.next

    return p1


s = SLinkedList()

nums = [1, 2, 8, 6, 5, 2, 7, 6, 5, 9, 2, 10]
nums = [11,22,33]

for num in nums:
    if not s.head:
        s.head = Node(num)
        curr = s.head

    else:
        n = Node(num)
        curr.next = n 
        curr = n
        
while True:
    k = input('Distance from end: ')

    try:
        k = int(k)
        break
    except ValueError:
        print('Please enter a valid integer: ')

    print(s)
    print(kth_to_last_element(s, k))