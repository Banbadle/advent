from collections import defaultdict
with open("input.txt") as f:
    positions = [int(line.rstrip()[-1]) for line in f]
    initial_positions = tuple(positions)

# Part 1
scores = [0,0]
num_turns = 0
while True:
    for player in [0,1]:
        positions[player] = ((positions[player] + 6 - num_turns - 1) % 10) + 1
        scores[player] += positions[player]
        num_turns += 1
        if scores[player] >= 1000:
            break
    else: continue
    break

print(num_turns * 3 * min(scores))
    
# Part 2
num_combs = {i:0 for i in range(3,10)}
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            num_combs[i+j+k] += 1

num_wins = [0,0]
game_states = defaultdict(int)
game_states[(initial_positions, (0,0), 0)] = 1

while game_states:
    new_game_states = defaultdict(int)
    for (positions, scores, player), frequency in game_states.items():
        for roll, combs in num_combs.items():
            new_scores = list(scores)
            new_positions = list(positions)
            
            new_positions[player] = ((positions[player] + roll - 1) % 10) + 1
            new_scores[player] += new_positions[player]
            
            if new_scores[player] >= 21:
                num_wins[player] += frequency * combs
            else:
                new_game_states[(tuple(new_positions), tuple(new_scores), not player)] += frequency * combs
                
    game_states = new_game_states
  
print(max(num_wins))      