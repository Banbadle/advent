from math import sqrt
from datetime import datetime
first = datetime.now()
with open("input.txt") as f:
    x, y = f.readline()[15:].split(", y=")
    x_range, y_range = [int(i) for i in x.split("..")], [int(j) for j in y.split("..")]
    
# Part 1
y_max = ((-y_range[0]-1) * (-y_range[0])) // 2
print(y_max)

# Part 2
def get_y_step_range(vy):
    y_step_ranges = [sqrt(((vy)*(vy+1)) + 0.25 - (2*(y_val))) + 0.5 - vy for y_val in y_range]
    range_ints = (int(y_step_ranges[1]-1), int(y_step_ranges[0])+1)
    # range_ints = (int(y_step_ranges[1]-1), int(y_step_ranges[0])+1)
    return range(*range_ints)

vx_ranges = (int((1 + sqrt(1 + 8*x_range[0])) / 2),     x_range[1]+1)

def get_x_from_steps(vx, steps):
    steps = min(steps, vx)
    return int(((2*vx + 1 - steps) * (steps))//2)

def get_y_from_steps(vy,steps):
    return int(((2*vy + 1 - steps) * (steps)) // 2)

velocity_list = []

for vy in range(-y_range[0] + 1):
    vy_step_range = (get_y_step_range(vy))
    # print(vy)
    # print(vy_step_range)
    for vx in range(*vx_ranges):
        for start_step in (0,2*vy+1) if vy != 0 else (0,):
            sign = -1 if start_step == 0 else 1
            y_step_list = [start_step + vy_step for vy_step in vy_step_range]
            
            for step_count in y_step_list:
                x_val = get_x_from_steps(vx, step_count)
                y_val = get_y_from_steps(sign*vy, step_count)
                
                if x_val >= x_range[0] and x_val <= x_range[1] and y_val >= y_range[0] and y_val <= y_range[1]:
                    # print(vx,vy,start_step)
                    velocity_list.append((vx,sign*vy))
                    break
            else:
                continue
            
print(len(velocity_list))
