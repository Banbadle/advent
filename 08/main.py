
with open("input.txt") as f:
    char_list, outputs = zip(*[[[frozenset(a) for a in c.split()], [frozenset(b) for b in o.split()]] for c,o in [line.rstrip().split("|") for line in f]])
    
print(sum([len([a for a in out if len(a) in {2,3,4,7}]) for out in outputs]))


length_to_num = {2:1, 3:7, 4:4, 7:8}
total = 0
for line in zip(char_list, outputs):
    num_to_chars = [0]*10
    fives_sixes = {5:[], 6:[]}
    for chars in line[0]:
        if len(chars) in length_to_num:
            num_to_chars[length_to_num[len(chars)]] = chars
        else:
            fives_sixes[len(chars)].append(chars)
            
    for six in fives_sixes[6]:
        if not num_to_chars[1].issubset(six):
            num_to_chars[6] = six
        elif num_to_chars[4].issubset(six):
            num_to_chars[9] = six
        else:
            num_to_chars[0] = six
        
    for five in fives_sixes[5]:
        if num_to_chars[1].issubset(five):
            num_to_chars[3] = five
        elif num_to_chars[9].issuperset(five):
            num_to_chars[5] = five
        else:
            num_to_chars[2] = five
             
    total += int("".join([[str(i) for i in range(0,10) if item == num_to_chars[i]][0] for item in line[1]]))
        
print(total)
