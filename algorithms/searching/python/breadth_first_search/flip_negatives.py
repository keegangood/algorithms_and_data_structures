from collections import deque
from random import randint

'''

'''

class FlipNegatives:
  def __init__(self, matrix):
    self.matrix=matrix
    self.rows = len(matrix)
    self.cols = len(matrix[0])


  def in_bounds(self, cell):
    y,x = cell
    return (0 <= y < self.rows) and (0 <= x < self.cols)

  def get_neighbors(self, cell):
    y,x = cell
    neighbors = [
      (y+1, x),
      (y-1, x),
      (y, x + 1), 
      (y, x - 1)
    ]
    
    return [n for n in neighbors if self.in_bounds(n)]
    
  def find_positives(self):
    positives = deque()
    for y in range(self.rows):
      for x in range(self.cols):
        cell = self.matrix[y][x]
        if cell > 0:
          positives.append((y,x))
    
    return positives

  def flip(self):
        Q = self.find_positives()
        passes = 0
        
        while Q:
            q = Q.copy()
            Q.clear()
            new_q = deque()
            
            while q:

                cell = q.popleft()

                y,x = cell
                if self.matrix[y][x] < 0:
                    self.matrix[y][x] *= -1

                neighbors = self.get_neighbors(cell)
                
                for neighbor in neighbors:
                    y,x = neighbor
                    
                    if self.matrix[y][x] < 0:
                        self.matrix[y][x] *= -1

                        next_neighbors = self.get_neighbors(neighbor)

                        new_q.extend(next_neighbors)

                print(f'{new_q = }')
            Q = new_q.copy()
            new_q.clear()
            passes += 1
    
        for row in self.matrix:
            print(row)

        return passes

         
mat = [
  [-1, -9, 0, -1, 0],
  [-8, -3, -2, 9, -7],
  [2, 0, 0, -6, 0],
  [0, -7, -3, 5, -4]
]

mat = [
  [-1, -1, 0, -1, 0, -1, 0, -1, 0],
  [0,  -1, 0, -1, 0, -1, 0, -1, 0],
  [-1, -1, -1, 9, -1, -1, 0, -1, 0],
  [2, 0, 0, -6, 0, -1, 0, -1, 0],
  [0, -7, -3, 5, -4, -1, 0, -1, 0]
]

flip = FlipNegatives(mat)

print(flip.flip())