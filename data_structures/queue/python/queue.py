from sys import maxsize

class Queue:
    def __init__(self, max_items=10, *items):
        self.items = list(items) or []
        self.MAXSIZE = maxsize

    def is_full(self):
        return len(self.items) == self.MAXSIZE

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        if len(self.items) == self.MAXSIZE:
            raise OverflowError('Max size exceeded.')

        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

        return None

    def __repr__(self):
        return str(self.items)

# ------------------------------------------------------------- #

def main():

    q = Queue()
    print('Queue Manipulation\n------------------\n')

    while True:
        options = {
            '1': 'Enqueue',
            '2': 'Dequeue',
            '3': 'View first',
            '4': 'Exit'
        }

        print(f'\nQueue: {q}')

        print('\nEnter the number of the operation you would like to perform: \n')
        for number, option in options.items():
            print(f'{number}: {option}')
        
        selection = input('\n> ')

        if selection == '1':
            while True:
                new_item = input('\nEnter the item to enqueue or "done" to continue: \n> ')
                
                if new_item == 'done':
                    break
                
                q.enqueue(new_item)

                print(f'\nQueue: {q}')
                
        elif selection == '2':
            q.dequeue()

        elif selection == '3':
            first = q.peek()

            if not first:
                print('The queue is empty.')
            else:
                print(f'First item: {first}')

        elif selection == '4':
            break

if __name__ == '__main__':
    main()