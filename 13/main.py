with open("input.txt") as f:
    input_text = f.readlines()

split_ind = input_text.index("\n")
coordinates = set((int(x), int(y)) for x,y in [line.split(",") for line in input_text[:split_ind]])
folds = [(xy, int(val)) for xy, val in [line.split("fold along ")[1].split("=") for line in input_text[split_ind+1:]]]

def fold_coordinates(coords, fold_xy, fold_val):
    new_coordinates = set()
    for pt in coords:
        new_pt = list(pt)
        
        index = 0 if fold_xy == "x" else 1
        if new_pt[index] > fold_val:
            new_pt[index] = 2*fold_val - new_pt[index]  
  
        new_coordinates.add(tuple(new_pt))
        
    return new_coordinates
    
#Part 1
print(len(fold_coordinates(coordinates, *folds[0])))

#Part 2
final_coordinates = coordinates
for fold in folds[0:]:
    final_coordinates = fold_coordinates(final_coordinates, *fold)
    
maxx, maxy = (max(x for x,_ in final_coordinates), max(y for _,y in final_coordinates))

grid = [["⬜" for i in range(maxx+1)] for j in range(maxy+1)]
for x,y in final_coordinates:
    grid[y][x] = "⬛"
    
for row in grid:
    print("".join(row))