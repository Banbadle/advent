with open("input.txt") as f:
    chunk_list = [line.rstrip() for line in f]
    
open_to_close = {"(":")",  "[":"]", "{":"}", "<":">"}

# Part 1
close_to_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
points = 0
incomplete_stacks = []
for chunk in chunk_list:
    stack = []
    for char in chunk:
        if char in open_to_close:
            stack.append(char)
        else:
            if open_to_close[stack[-1]] == char:
                stack.pop()
            else:
                points += close_to_points[char]
                break
    else:        
        incomplete_stacks.append(stack)
    
print(points)

# Part 2
open_to_points = {"(": 1, "[": 2, "{": 3, "<": 4}
points_list = []  
for stack in incomplete_stacks:
    chunk_points = 0
    for char in reversed(stack):
        chunk_points = 5*chunk_points + open_to_points[char]
    
    points_list.append(chunk_points)
        
print(sorted(points_list)[len(points_list)//2])