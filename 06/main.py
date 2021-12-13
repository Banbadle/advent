def get_num_fish(days=80):
    fish_list = [0]*9
    with open("input.txt") as f:
        for i in [int(num) for num in next(f).split(",")]: fish_list[i]+=1 
    
    for pointer in [(day)%9 for day in range(0, days)]:
        fish_list[pointer-2] += fish_list[pointer]
    
    return(sum(fish_list))

#PART 1
print(get_num_fish(80))
#PART 2
print(get_num_fish(256))