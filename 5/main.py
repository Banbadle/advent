#PART 1
with open("input.txt") as f:
    points = [[tuple(int(x) for x in pts.split(",")) for pts in line.split(" -> ")] for line in f]
    
point_map = dict()
for pt in points:
    if (pt[0][1] == pt[1][1]) != (pt[0][0] == pt[1][0]):
        for x in range(pt[0][0], pt[1][0] + (-1 if pt[0][0] > pt[1][0] + 1 else 1), (-1 if pt[0][0] > pt[1][0] + 1 else 1) ):
            for y in range(pt[0][1], pt[1][1] + (-1 if pt[0][1] > pt[1][1] + 1 else 1),  (-1 if pt[0][1] > pt[1][1] + 1 else 1)):
                point_map[(x,y)] = point_map[(x,y)] + 1 if (x,y) in point_map else 1

print(len([x for x in point_map if point_map[x] > 1]))

#PART 2
with open("input.txt") as f:
    points = [[tuple(int(x) for x in pts.split(",")) for pts in line.split(" -> ")] for line in f]
    
point_map = dict()
for pt in points:
    if (pt[0][1] == pt[1][1]) != (pt[0][0] == pt[1][0]):
        for x in range(pt[0][0], pt[1][0] + (-1 if pt[0][0] > pt[1][0] + 1 else 1), (-1 if pt[0][0] > pt[1][0] + 1 else 1) ):
            for y in range(pt[0][1], pt[1][1] + (-1 if pt[0][1] > pt[1][1] + 1 else 1),  (-1 if pt[0][1] > pt[1][1] + 1 else 1)):
                point_map[(x,y)] = point_map[(x,y)] + 1 if (x,y) in point_map else 1
    else:
        for (x,y) in zip(range(pt[0][0], pt[1][0] + (-1 if pt[0][0] > pt[1][0] + 1 else 1), (-1 if pt[0][0] > pt[1][0] + 1 else 1) ), range(pt[0][1], pt[1][1] + (-1 if pt[0][1] > pt[1][1] + 1 else 1),  (-1 if pt[0][1] > pt[1][1] + 1 else 1))):
            point_map[(x,y)] = point_map[(x,y)] + 1 if (x,y) in point_map else 1

print(len([x for x in point_map if point_map[x] > 1]))