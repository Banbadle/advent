class Board():
    
    def __init__(self, array):
        self.grid = dict()
        self.rows = [0,0,0,0,0]
        self.columns = [0,0,0,0,0]
        self.unmarked = 0
        for i in range(0,len(array)):
            for j in range(0,len(array[0])):
                
                self.grid[array[i][j]] = (i,j)
                self.unmarked += array[i][j]
            
    def add(self, num):
        if num in self.grid:
            i,j = self.grid[num]
            self.rows[i] += 1
            self.columns[j] += 1
            self.unmarked -= num
            if self.rows[i] == 5 or self.columns[j] == 5:
                return True
        return False
      
#Part 1  
with open("input.txt") as f:
    bingo_list = [int(x) for x in next(f).rstrip().split(",")]
    next(f)

    grid_list = [Board([[int(x) for x in line.split()] for line in grid.split("\n")]) for grid in f.read().split("\n\n")]
              
for num in bingo_list:
    for grid in grid_list:
        if grid.add(num) == True:
            print(grid.unmarked * num)
            break
    else:
        continue
    break

#Part 2
with open("input.txt") as f:
    bingo_list = [int(x) for x in next(f).rstrip().split(",")]
    next(f)

    grid_list = [Board([[int(x) for x in line.split()] for line in grid.split("\n")]) for grid in f.read().split("\n\n")]

winner_list = []
for num in bingo_list:
    for i in range(0, len(grid_list)):
        grid = grid_list[i]
        if grid.add(num) == True:
            if i not in [x for x,_ in winner_list]:
                winner_list.append((i, grid.unmarked * num))
                
print(winner_list[-1][-1])