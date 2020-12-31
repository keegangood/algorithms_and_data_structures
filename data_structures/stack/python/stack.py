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



def main():

    s = Stack()
    print('Stack Manipulation\n------------------\n')

    while True:
        options = {
            '1': 'Add item',
            '2': 'Remove item',
            '3': 'View first',
            '4': 'Exit'
        }

        print(f'Stack: {s}')

        print('\nEnter the number of the operation you would like to perform: \n')
        for number, option in options.items():
            print(f'{number}: {option}')
        
        selection = input('\n> ')

        if selection == '1':
            while True:
                new_item = input('\nEnter the item to add or "done" to continue: \n> ')
                
                if new_item == 'done':
                    break
                
                s.push(new_item)

                print(f'Stack: {s}')
                
        elif selection == '2':
            s.pop()

        elif selection == '3':
            first = s.peek()

            if not first:
                print('The stack is empty.')
            else:
                print(f'First item: {first}')

        elif selection == '4':
            break

if __name__ == '__main__':
    main()