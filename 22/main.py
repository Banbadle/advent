from collections import defaultdict
import re
with open("input.txt") as f:
    instructions = [re.split(" x=|,y=|,z=|\\.\\.", line.rstrip()) for line in f]
    instructions = [[1 if line[0] == "on" else 0] + [int(num) for num in line[1:]] for line in instructions]
    
# Part 1    
def range_50(x1,x2):
    return range(max(-50, x1), min(51, x2+1))
    
state_dict = defaultdict(int)
for state, x1, x2, y1, y2, z1, z2 in instructions:
    for x in range_50(x1,x2):
        for y in range_50(y1,y2):
            for z in range_50(z1,z2):
                state_dict[(x,y,z)] = state
                
print(sum([1 for s in state_dict.values() if s==1]))

#Part 2
for i1 in range(instructions):
    state, x1, x2, y1, y2, z1, z2 = instructions[i1]
    volume = (x2-x1+1) * (y2-y1+1) * (z2-z1+1)
    
    for state_n, x1_n, x2_n, y1_n, y2_n, z1_n, z2_n inreinstructions[:i1].reverse():
        overlap_volume = 1
        for a1, a2, b1, b2 in ((x1, x2, x1_n, x2_n), (y1, y2, y1_n, y2_n), (z1, z2, z1_n, z2_n))
            overlap_volume *= max(min(a2, b2) - max(a1, b1) + 1, 0)
    
    
    # + +: + volume - overlap
    # + -: - overlap
    # - -: None
    # - +: + volume
    