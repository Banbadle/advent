from collections import defaultdict

with open("input.txt") as f:
    input_polymer = f.readline().rstrip()
    f.readline()
    
    insert_pairs = dict()
    for line in f:
        pair, insert = line.rstrip().split(" -> ")
        insert_pairs[pair] = (pair[0]+insert, insert+pair[1])
        
def polymerization(polymer, levels):
    pair_counts, letter_counts = defaultdict(int), defaultdict(int)    
    
    for i in range(len(polymer)-1):
        pair_counts[polymer[i:i+2]] += 1            

    for i in range(levels):
        new_pair_counts = defaultdict(int)      
        for pair in pair_counts:
            for new_pair in insert_pairs[pair]:
                new_pair_counts[new_pair] += pair_counts[pair]
                
        pair_counts = new_pair_counts

    for pair in pair_counts:
        letter_counts[pair[0]] += pair_counts[pair]
    letter_counts[polymer[-1]] += 1

    return (max(letter_counts.values()) - min(val for val in letter_counts.values() if val!=0))

# Part 1
print(polymerization(input_polymer,10))

# Part 2
print(polymerization(input_polymer,40))