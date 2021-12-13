with open("input.txt") as f:
    num_list = [int(line) for line in f]

def count(offset=1):
    count = 0
    for i in range(len(num_list) - offset):
        if num_list[i + offset] > num_list[i]:
            count+=1
            
    return(count)

#Part 1
print(count(1))

#Part 2
print(count(3))