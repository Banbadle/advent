def next_step(grid):

    increment_queue = [(i,j) for i in range(len(grid)) for j in range(len(grid[0]))]
    for i,j in increment_queue:
        grid[i][j] += 1
        if grid[i][j] == 10: 
            flash_grid = [(x,y) for x in range(i-1, i+2) for y in range(j-1,j+2) if (x,y) != (i,j)]
            increment_queue += [(x,y) for x,y in flash_grid if x in range(len(grid)) and y in range(len(grid[0]))]
            
    flashes = 0
    for i,j in [(i,j) for i in range(len(grid)) for j in range(len(grid[0]))]:
        if grid[i][j] >= 10:
            grid[i][j] = 0 
            flashes += 1
            
    return flashes

#Part 1 
with open("input.txt") as f:
    grid_1 = [[int(x) for x in list(line.rstrip())] for line in f]
    
flashes = 0
for _ in range(100):
    flashes += next_step(grid_1)
    
print(flashes)

#Part 2
with open("input.txt") as f:
    grid_2 = [[int(x) for x in list(line.rstrip())] for line in f]
    
steps = 0
grid_size = len(grid_2) * len(grid_2[0])
while True:
    flashes = next_step(grid_2)
    steps += 1
    if flashes == grid_size:
        print(steps)
        break
