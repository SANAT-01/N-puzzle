import tkinter as tk
from tkinter import messagebox
import heapq
import numpy as np

# Copy the previous code for inp, heuristic_val, ways, and solve functions here

def draw_board(puzzle, canvas):
    print(puzzle)
    for i in range(3):
        for j in range(3):
            canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, outline="black")
            # print(puzzle[i])
            # print(puzzle[i][j])
            if puzzle[i][j] != 0:
                canvas.create_text((j + 0.5) * 50, (i + 0.5) * 50, text=str(puzzle[i][j]))
    print(True)

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
  sol = []
  Heap = [(0,start)]
  heapq.heapify(Heap)
  length = len(start)
  visited = []
  itr = True
  while itr and Heap:
    curr = heapq.heappop(Heap)[1]
    print(np.array(curr))
    print()
    sol.append(curr)
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
    
  sol.append(neighbour)
  return sol

def solve_puzzle():
    if len(start) != len(start[0]) or len(goal) != len(goal[0]):
        messagebox.showerror("Error", "Dimensions are not correct!")
        return
    
    solution = solve(start, goal)

    # Create the Tkinter window
    window = tk.Tk()
    window.title("N-Puzzle Game")

    # Create the Canvas to draw the puzzle board
    canvas = tk.Canvas(window, width=len(start[0]) * 50, height=len(start) * 50)
    canvas.pack()

    # Draw the start state
    print(start)
    draw_board(start, canvas)

    # Animate the solution
    for state in solution:
        canvas.delete("all")
        draw_board(state, canvas)
        canvas.update()
        canvas.after(100)

    messagebox.showinfo("Success", "Puzzle Solved!")

    window.mainloop()

start = [[8, 2, 0], 
         [4, 5, 3],
         [7, 1, 6]]

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]

solve_puzzle()
