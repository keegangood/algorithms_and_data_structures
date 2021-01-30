from SLinkedList import SLinkedList, Node

def remove_duplicates(linked_list):
    '''
    remove all duplicates from a linked list
    Time complexity: O(n)
    Space complexity: O(n - duplicates)
    '''
    items = {}

    curr = linked_list.head
    prev = None
    while curr is not None:
        if not items.get(curr.val):
            items[curr.val] = curr
            prev = curr
        else:
            prev.next = curr.next

        if curr.next:
            curr = curr.next
        else:
            return linked_list

s = SLinkedList()

nums = [1, 2, 8, 6, 5, 2, 7, 6, 5, 9, 2, 10]

for num in nums:
    if not s.head:
        s.head = Node(num)
        curr = s.head

    else:
        n = Node(num)
        curr.next = n 
        curr = n
        
print(s)
print(remove_duplicates(s))