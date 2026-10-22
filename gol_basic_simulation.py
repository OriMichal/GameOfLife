#array of arrays?
import time
import os

with open("seed.txt", "r") as f:
    grid = [[int(cell) for cell in line.split()] for line in f.readlines()]

#counting live neighbors via summation?
#edge cases: maybe use the general counting method on them and catch errors?(spoiler: did not work)
def live_neighbors(array,y,x):
     sum = 0
     if x<len(array[0])-1 and y< len(array)-1:
        if array[y+1][x+1] == 1:
            sum = sum+1
     if x<len(array[0])-1:
         if array[y][x+1] == 1:
            sum = sum+1
     if y<len(array)-1:
         if array[y+1][x] == 1:
            sum = sum+1
     if x>0 and y>0:
         if array[y-1][x-1] == 1:
             sum = sum+1
     if x>0:
         if array[y][x-1] == 1:
             sum = sum+1
     if y>0:
         if array[y-1][x] == 1:
             sum = sum+1
     if x>0 and y<len(array)-1:
         if array[y+1][x-1] == 1:
             sum = sum+1
     if x<len(array[0])-1 and y>0:
         if array[y-1][x+1] ==1:
             sum = sum+1
     return sum

def simulation_gen(array):
    new_array = [[0 for col in range(len(array[0]))] for row in range(len(array))]
    for y in range(0,len(array)):
        for x in range(0,len(array[0])):
            if array[y][x] == 1:
                if live_neighbors(array,y,x) < 2:
                    new_array[y][x] = 0
                if 2<=live_neighbors(array,y,x) <= 3:
                    new_array[y][x] = 1
                if live_neighbors(array,y,x) > 3:
                    new_array[y][x] = 0
            if array[y][x] == 0 and live_neighbors(array,y,x) == 3:
                new_array[y][x] = 1
    return new_array


def render(array, gen):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in array:
        print("".join("■ " if cell == 1 else ". " for cell in row))
    print(f"gen {gen}")

GENERATIONS = 500
DELAY = 0.4

for gen in range(GENERATIONS):
    render(grid, gen)
    time.sleep(DELAY)
    grid = simulation_gen(grid)

#used DeepSeek for graphics, rest of the code is by me.

















    


