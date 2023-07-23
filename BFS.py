from inspect import stack
import numpy as np 
import math

def inp():
  lg = int(input("Enter number of tiles "))
  lg = ( math.sqrt(lg + 1))
  if int(lg) != lg :
    raise Exception(" Such tiles puzzle won't exist !! ") 

  lg = int(lg)
  
  print("Enter the start ")
  print("""example : 3X3
  1 2 3
  7 4 6
  5 0 8""")

  start = []
  for i in range(lg):
    ip = str(input())
    st = list(map(int,ip.split()))
    start.append(st)

  print("Enter goal")
  goal = []
  for i in range(lg):
    ip = str(input())
    st = list(map(int,ip.split()))
    goal.append(st)

  return start,goal


def ways(grid,n):
  steps_x = [0,-1,1,0]
  steps_y = [1,0,0,-1]
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
    #print(np.array(block))
    place.append(str(block))
  return place

def push(lst,i):
  lst.append(None)
  for j in range(len(lst)-1,0,-1):
    lst[j] = lst[j-1]
    #print(lst)
  lst[0] = i
  print(lst)
  return lst

def puzzle(root,goal):
  visited = [] # List to keep track of visited nodes.
  stack = []
  visited.append(root)
  stack.append(root)
  length = len(root)
  count = 0
  flag = False
  while stack:
    count += 1
    s = stack.pop(0)
    neighbours = ways(s,length)
    #print (np.array(s),neighbours,"--",queue,"--",visited)
    print(np.array(s))
    print()
    for neighbour in neighbours :
      state = eval(neighbour)
      if state not in visited:
        if state == goal:
          flag = True
          break
        visited.append(state)
        stack.append(state)
        # push(stack,state)
    if flag:
      break
  return state

start = [[1,3,2], 
         [0,4,8],
         [7,5,6]]

start2 = [[8,2,0], 
         [4,5,3],
         [7,1,6]]

goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

# Driver Code

# start,goal = inp()
print("--------------")
print("Start state :\n",np.array(start))
print("Goal state :\n",np.array(goal))
print("--------------")

if len(start) == len(start[0]) and len(goal) == len(goal[0]):
  ed = np.array(puzzle(start,goal))
  print(ed)

else:
  print("Dimension are not correct")
