with open("input.txt") as f:
    connection_tuple = tuple(line.rstrip().split("-") for line in f)
    
caves = set(sum(connection_tuple, []))
small_caves = set([node for node in caves if node.lower() == node])
connection_dict = {node: [] for node in caves}

for a,b in connection_tuple:
    connection_dict[a].append(b)
    connection_dict[b].append(a)
  
def find_paths(path=["start"], repeats=0):
    path_list = []
    current_cave = path[-1]
    
    if current_cave == "end":
        return [path]
    
    for next_cave in [cave for cave in connection_dict[current_cave] if (cave not in small_caves or cave not in path or repeats > 0) and cave!= "start"]:
        next_repeats = repeats - 1*(next_cave in path and next_cave in small_caves)
        new_path = path + [next_cave]
        path_list += find_paths(new_path, next_repeats)
       
    return path_list
         
#Part 1
print(len(find_paths()))

#Part 2
print(len(find_paths(repeats=1)))
