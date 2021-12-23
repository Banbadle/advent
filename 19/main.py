from collections import defaultdict

with open("input.txt") as f:
    scanner_list = "".join(f.readlines()).split("\n\n")
    scanner_list = tuple(tuple(tuple(int(num) for num in coords.split(",")) for coords in scanner.split("\n")[1:]) for scanner in scanner_list)

def get_rotations():
    cycle_x = ((1,1),(2,1),(1,-1),(2,-1))*2
    cycle_y = ((0,-1),(2,1),(0,1),(2,-1))*2
    cycle_z = ((1,1),(0,-1),(1,-1),(0,1))*2
    
    get_up_cycle = [cycle_x, cycle_y, cycle_z]
    
    rotations = []
    
    for forward in [0,1,2]:
        cycle = get_up_cycle[forward]
        for sign in [1,-1]:
            for rotate_index in range(4):
                
                up = cycle[rotate_index]
                side = cycle[rotate_index + sign]
                new_rotation = ((forward, sign), up, side)
            
                rotations.append(new_rotation)
                
    return rotations

rotation_list = get_rotations()
            
def rotate(x, y, z, rotation):
    new_pos = [0,0,0]
    for i in range(0,3):
        axis, sign = rotation[i]
        new_pos[i] = (x,y,z)[axis] * sign
        
    return tuple(new_pos)


found_scanners = {0: (scanner_list[0], (0,0,0))} # index: beacon locations (rotated)
found_scanner_indexes = [0]

def sum_vectors(a,b):
    return tuple(sum(tup) for tup in (zip(a,b)))

while len(found_scanners) < len(scanner_list):
    for i1 in found_scanner_indexes:
        scanner_1, scanner_1_pos = found_scanners[i1]
        for i2 in range(len(scanner_list)):
            if i2 in found_scanners: continue
            scanner_2 = scanner_list[i2]  
            
            for rotation in rotation_list:
                difference_counts = defaultdict(int)
                for x1,y1,z1 in scanner_1:
                    for x2,y2,z2 in scanner_2:
                        
                        x2r, y2r, z2r = rotate(x2, y2, z2, rotation)
                        diff_vector = (x1 - x2r, y1 - y2r, z1 - z2r)
                        
                        difference_counts[diff_vector] += 1
                            
                        if difference_counts[diff_vector] >= 12:
                            
                            rotated_scanner = list(sum_vectors(rotate(x,y,z,rotation), diff_vector) for x,y,z in scanner_2)
                            found_scanners[i2] = (rotated_scanner, diff_vector)
                            found_scanner_indexes.append(i2)
                            break
                        
                    else: continue
                    break
                else: continue
                break

                        
# Part 1
beacon_set = set()
for scanner,_ in found_scanners.values():
    for beacon_pos in scanner:
        beacon_set.add(beacon_pos)
print(len(beacon_set))
                    
# Part 2
distances = []
for _, scanner_1_pos in found_scanners.values():
    for _, scanner_2_pos in found_scanners.values():
        new_dist = sum(abs(a-b) for a,b in zip(scanner_1_pos, scanner_2_pos))
        distances.append(new_dist)
        
print(max(distances))