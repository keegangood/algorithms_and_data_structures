from collections import deque

'''
Task:

Given a Maze in the form of a rectangular matrix, filled with either
'O', 'X' or 'M', where 'O' represents an open cell, 'X' represents
a blocked cell and 'M' represents landmines in the maze, we need to
find the shortest distance of every open cell in the maze from its 
nearest mine.

Time Complexity
O(n) - find all mines + O(n - number_of_Xs)
O(n^2 - number_of_Xs)

Space Complexity
O(n)
'''

class NearestMine:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
    
    def find_mines(self):
		'''Loop through all cells and add those containing mines to a deque'''
        mines = deque()
        for y in range(self.rows):
            for x in range(self.cols):
                if self.maze[y][x] == 'M':
                    mines.append((y,x))

        return mines

    def in_bounds(self, cell):
		'''return True if the cell is in the maze, otherwise False'''
        y,x = cell
        return (0 <= y < self.rows) and (0 <= x < self.cols)


    def get_neighbors(self, cell):
		'''Return a deque containing the valid neighbors of a given cell'''
        y,x = cell
        neighbors = [
            (y+1, x),
            (y-1, x),
            (y, x+1), 
            (y, x-1)
        ]

		# filter out neighbors that aren't within the maze dimensions
        neighbors = deque([n for n in neighbors if self.in_bounds(n)])
        return neighbors                

    def find_nearest_mines(self):
        Q = self.find_mines() # get the locations of the mines
        level = 1 # counter for distance from nearest mine
		
		# while there are cells to be checked
        while Q:
            q = Q.copy() # make a copy of the cells to be checked
            Q.clear() # erase original 

            next_level = deque()
            while q:
                cell = q.popleft() # remove first cell
                neighbors = self.get_neighbors(cell) # get its neighbors

                for neighbor in neighbors:
                    y,x = neighbor
					
					# if the neighbor's value is 'O'
                    if self.maze[y][x] == 'O':
						# add the neighbor to be checked
                        next_level.append(neighbor)
						# make the neighbors value its distance from nearest mine
                        self.maze[y][x] = f'{level}'

					# if the neighbor isn't visitable
                    elif self.maze[y][x] == 'X':
                        self.maze[y][x] = '*'

					# if the neighbor is a bomb
                    elif self.maze[y][x] == 'M':
						# change M to B to show the cell has been processed
                        self.maze[y][x] = 'B'
			
			# increase level count and set Q to the new set of neighbors
            level += 1
            Q = next_level
        
		# return the augmented maze at the end
        return self.maze


maze1 = [
    ['O', 'M', 'O', 'O', 'X'],
    ['O', 'X', 'X', 'O', 'M'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'M', 'O', 'O'],
    ['O', 'X', 'X', 'M', 'O']
]

N = NearestMine(maze1)

result = N.find_nearest_mines()

for row in result:
    print(row)