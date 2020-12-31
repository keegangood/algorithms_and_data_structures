class Stack:
    def __init__(self, items=None):
        '''Initialize an instance of a stack with default items, if provided'''
        self.items = [] if items is None else items

    def is_empty(self):
        '''Return boolean denoting whether the Stack is empty or not'''
        return self.items == [] 

    def push(self, item):
        '''Add item to the top of the Stack'''
        self.items.append(item)

    def pop(self):
        '''Remove item from the top of the Stack'''
        return self.items.pop() if not self.is_empty() else 'The Stack is empty.'

    def peek(self):
        '''View the top item of the Stack'''
        return self.items[0] if not self.is_empty() else 'The Stack is empty.'

    def __repr__(self):
        '''Return the Stack's items and the first item in the Stack'''
        return f'{self.items}'


