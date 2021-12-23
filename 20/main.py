with open("input.txt") as f:
    iea = "".join(("0" if char == "." else "1") for char in f.readline().rstrip())
    f.readline()
    input_image = ["".join(("0" if char == "." else "1") for char in line.rstrip()) for line in f]


def pad_image(input_image, char):
    return [char * (len(input_image[0]) + 4)]*2 + [char*2 + line + char*2 for line in input_image] + [char * (len(input_image[-1]) + 4)]*2

def enhance(input_image, inf_char="0"):
    input_image = pad_image(input_image, inf_char)  
    output_image = []
    for x in range(1, len(input_image) - 1):
        next_line = ""
        for y in range(1, len(input_image[0]) - 1):
            index = ""
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    index += input_image[i][j]
                    
            next_line += iea[int(index, 2)]
        output_image.append(next_line)
        
    next_inf_char = iea[0] if inf_char == "0" else iea[-1]
    return output_image, next_inf_char
        
# Part 1
inf_char = "0"
for i in range(2):
    input_image, inf_char = enhance(input_image, inf_char)

print(sum([len([char for char in line if char == "1"]) for line in input_image]))

# Part 2
for i in range(50-2):
    input_image, inf_char = enhance(input_image, inf_char)

print(sum([len([char for char in line if char == "1"]) for line in input_image]))