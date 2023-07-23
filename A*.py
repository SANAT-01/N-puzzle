from inspect import stack
import numpy as np 
import heapq
import math

def inp():
  lg = int(input("Enter number of tiles "))
  lg = ( math.sqrt(lg + 1))
  if int(lg) != lg :
    raise Exception(" Such tiles puzzle won't exist !! ") 

  lg = int(lg)
  print("Enter the start state")
  print("""example : 3X3
  1 2 3
  7 4 6
  5 0 8""")

  start = []
  for i in range(lg):
    ip = str(input())
    st = list(map(int,ip.split()))
    start.append(st)

  print("Enter goal state")
  goal = []
  for i in range(lg):
    ip = str(input())
    st = list(map(int,ip.split()))
    goal.append(st)
  return start,goal


def heuristic_val(puz,goal):
  count = 0
  lg = len(puz)
  for i in range(lg):
    for j in range(lg):
      if puz[i][j] != goal[i][j]:
        count += 1

  return count


def ways(grid,n):
  steps_x = [0,-1,1,0]
  steps_y = [1,0,0,-1]
  for x,y in enumerate(grid):
    #print(y)
    if 0 in y:
      ind = y.index(0)
      break
  y = ind
  place = []
  grid = str(grid)
  for a in range(4):
    block = eval(grid)
    ind_x = x + steps_x[a]
    ind_y = y + steps_y[a]
    if (ind_x < 0 or ind_x >= n) or (ind_y < 0 or ind_y >= n):
      continue
    block[ind_x][ind_y], block[x][y] = block[x][y], block[ind_x][ind_y]
    #print(np.array(block))
    place.append(str(block))
  return place

def solve(start,goal):
  Heap = [(0,start)]
  heapq.heapify(Heap)
  length = len(start)
  visited = []
  itr = True
  while itr and Heap:
    curr = heapq.heappop(Heap)[1]
    print(np.array(curr))
    print()
    neighbours = ways(curr,length)
    
    #print(neighbours)
    for neighbour in neighbours:
      neighbour = eval(neighbour)
      if neighbour not in visited:
        if neighbour == goal:
          itr = False
          break
        # h_val.append(heuristic_val(neighbour,goal))
        # ng.append(neighbour)
        visited.append(neighbour)
        h_val = heuristic_val(neighbour,start) + heuristic_val(neighbour,goal) 
        heapq.heappush(Heap, (h_val, neighbour))

    if not itr: # break because of reaching goal
      break

  return neighbour



start2 = [[1,3,2], 
         [0,4,8],
         [7,5,6]]

start = [[8,2,0], 
         [4,5,3],
         [7,1,6]]

goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

# Driver Code

# start,goal = inp()
print("------------")
print("start",np.array(start))
print()
print("goal",np.array(goal))
print("------------")

if len(start) == len(start[0]) and len(goal) == len(goal[0]):
  ed = np.array(solve(start,goal))
  print(ed)

else:
  print("Dimension are not correct")