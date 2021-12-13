with open("input.txt") as f:
    grid = [[int(x) for x in list(line.rstrip())] for line in f]

def get_adjacent(i,j):
    pts = ((i,j+1),(i+1,j),(i-1,j), (i,j-1))
    return list([(w,v) for w,v in pts if w in range(0,len(grid)) and v in range(0,len(grid[0]))])

#Part 1
low_points = []
for i,j in ((i,j) for i in range(0,len(grid)) for j in range(0, len(grid[0]))):
    is_low = True
    for x,y in get_adjacent(i,j):
        is_low = is_low and grid[x][y] > grid[i][j]
            
    if is_low:
        low_points.append((i,j))
        
print(sum([grid[x][y] for x,y in low_points]) + len(low_points))

#Part 2
basins = []
for low in low_points:
    new_basin = set([low])
    queue = get_adjacent(*low)
    for i,j in queue:
        if (i,j) in new_basin or grid[i][j] == 9:
            continue
        outside_pts = [pt for pt in get_adjacent(i,j) if pt not in new_basin]
        in_basin = True
        for x,y in outside_pts:
            in_basin = in_basin and grid[x][y] >= grid[i][j]
            
        if in_basin:
            new_basin.add((i,j))
            queue += outside_pts
            
    basins.append(new_basin)

        
basin_sizes = sorted([len(basin) for basin in basins])
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])