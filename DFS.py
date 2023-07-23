import numpy as np 
import math

def inp():
  lg = int(input("Enter number of tiles "))
  lg = ( math.sqrt(lg + 1))
  if int(lg) != lg :
    raise Exception(" Such tiles puzzle won't exist !! ") 

  lg = int(lg)

  print("Enter the start states")
  print("""example : 3X3
  1 2 3
  7 4 6
  5 0 8""")
  start = []
  for i in range(lg):
    ip = str(input())
    st = list(map(int,ip.split()))
    start.append(st)

  print("Enter goal states")
  goal = []
  for i in range(lg):
    ip = str(input())
    st = list(map(int,ip.split()))
    goal.append(st)

  return start,goal


def ways(grid,n):
  steps_x = [-1,1,0,0]
  steps_y = [0,0,1,-1]
  for x,y in enumerate(grid):
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
    place.append(str(block))
  return place
  
def puzzle(root,goal):
  visited = [] # List to keep track of visited nodes.
  queue = []
  visited.append(root)
  queue.append(root)
  length = len(root)
  count = 0
  flag = False
  while queue:
    count += 1
    s = queue.pop(-1)
    neighbours = ways(s,length)
    #print (np.array(s),neighbours,"--",queue,"--",visited)
    print (np.array(s))
    print()

    for neighbour in neighbours :
      state = eval(neighbour)
      if state not in visited:
        if state == goal:
          flag = True
          break
        visited.append(state)
        queue.append(state)
    if flag:
      break
  return state

start = [[1,2,3], 
         [0,4,6],
         [7,5,8]]

start2 = [[1,2,3], 
         [4,5,6],
         [7,0,8]]

start3 = [[2,5,8], 
         [1,4,6],
         [7,0,3]]

goal = [[1,2,3], 
         [4,5,6],
         [7,8,0]]

# Driver Code


# start,goal = inp()

print("-------------")
print("Start state :\n", np.array(start))
print("Goal state :\n", np.array(goal))
print("------------")

if len(start) == len(start[0]) and len(goal) == len(goal[0]):
  ed = np.array(puzzle(start,goal))
  print(ed)

else:
  print("Dimension are not correct")