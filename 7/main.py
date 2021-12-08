with open("input.txt") as f:
    positions = sorted([int(n) for n in next(f).split(",")])
    
#PART 1
median = positions[len(positions)//2]
fuel_cost = sum([abs(median - x) for x in positions])
print(fuel_cost)

#PART 2
mu = sum(positions)//len(positions)
fuel_cost1 = sum([(abs(x-(mu-1)) * (abs(x-(mu-1))+1)) // 2 for x in positions])
fuel_cost2 = sum([(abs(x-mu) * (abs(x-mu)+1)) // 2 for x in positions])
fuel_cost3 = sum([(abs(x-(mu+1)) * (abs(x-(mu+1))+1)) // 2 for x in positions])
print(min(fuel_cost1, fuel_cost2, fuel_cost3))