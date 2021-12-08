with open("input.txt") as f:
    positions = sorted([int(n) for n in next(f).split(",")])
    
#PART 1
median = positions[len(positions)//2]
fuel_cost = sum([abs(median - x) for x in positions])
print(fuel_cost)

#PART 2
mean = sum(positions)/len(positions)
fuel_costs = [sum([(abs(x-(mu)) * (abs(x-(mu))+1)) // 2 for x in positions]) for mu in range(int((mean-0.5)//1), int((mean+1.5)//1))]
print(min(fuel_costs))