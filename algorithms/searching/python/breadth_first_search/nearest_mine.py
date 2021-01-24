from collections import deque

'''
Task:

Given a Maze in the form of a rectangular matrix, filled with either
'O', 'X' or 'M', where 'O' represents an open cell, 'X' represents
a blocked cell and 'M' represents landmines in the maze, we need to
find the shortest distance of every open cell in the maze from its 
nearest mine.
'''

class NearestMine:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
    

    def in_bounds(self, cell):
        y,x = cell
        return (0 <= y < self.rows) and (0 <= x < self.cols)


    def get_neighbors(self, cell):
        y,x = cell
        neighbors = [
            (y+1, x),
            (y-1, x),
            (y, x+1), 
            (y, x-1)
        ]
        neighbors = deque([n for n in neighbors if self.in_bounds(n)])
        return neighbors                

    def find_nearest_mines(self):
        

maze = [
    ['O', 'M', 'O', 'O', 'X'],
    ['O', 'X', 'X', 'O', 'M'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'M', 'O', 'O'],
    ['O', 'X', 'X', 'M', 'O']
]

N = NearestMine(maze)

N.find_nearest_mines()