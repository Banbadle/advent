with open("input.txt") as f:
    grid = [[int(x) for x in list(line.rstrip())] for line in f]

def get_adjacent(i,j):
    pts = ((i,j+1),(i+1,j),(i-1,j), (i,j-1))
    return list([(x,y) for x,y in pts if x in range(0,len(grid)) and y in range(0,len(grid[0]))])

#Part 1
low_points = []
for i,j in ((i,j) for i in range(0,len(grid)) for j in range(0, len(grid[0]))):
    if all(grid[x][y] > grid[i][j] for x,y in get_adjacent(i,j)):
        low_points.append((i,j))
        
print(sum([grid[x][y] for x,y in low_points]) + len(low_points))

#Part 2
basins = []
for low in low_points:
    new_basin = set([low])
    queue = get_adjacent(*low)
    for i,j in queue:
        if (i,j) not in new_basin and grid[i][j] != 9:
            new_basin.add((i,j))
            queue += get_adjacent(i,j)
            
    basins.append(new_basin)
        
basin_sizes = sorted([len(basin) for basin in basins])
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])