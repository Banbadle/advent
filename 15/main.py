from collections import defaultdict

with open("input.txt") as f:
    grid_small = [[int(val) for val in line.rstrip()] for line in f]

def get_adjacent(i,j, grid):
    pts = ((i,j+1),(i+1,j),(i-1,j), (i,j-1))
    return list([(x,y) for x,y in pts if x in range(len(grid)) and y in range(len(grid[0]))])

def get_risk(grid):
    start, end = (0,0),  (len(grid)-1, len(grid[0])-1)
    
    risk_to_coords = defaultdict(list)
    risk_to_coords[0].append(start)       
    
    coords_to_risk = {(x,y): -1 for x in range(len(grid)+1) for y in range(len(grid[0])+1)}
                    
    risk = 0
    while True:
        for x,y in risk_to_coords[risk]:
            if coords_to_risk[(x,y)] != -1:
                continue
            coords_to_risk[(x,y)] = risk
            for i,j in get_adjacent(x,y, grid):
                risk_to_coords[risk + grid[i][j]].append((i,j))
                
        if coords_to_risk[end] != -1:   
            return risk
            
        risk += 1
        
            
# Part 1
print(get_risk(grid_small))     


# Part 2
int_list = list(range(1, 10))                               

grid_large = []   
for i in range(0,5):  

    for line in grid_small:
        next_line = []
        for j in range(0,5):
            next_line += list([int_list[(num + i + j - 1) % 9] for num in line])
            
        grid_large.append(next_line)

print(get_risk(grid_large))