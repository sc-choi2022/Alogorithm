import random as random
dwarf = []
height_sum = 0
for _ in range(9):
    dwarf.append(int(input()))

clue = sum(dwarf) - 100

while height_sum != clue:
    liar_guess = random.sample(dwarf,2)
    height_sum = sum(liar_guess)

for liar in liar_guess:
    dwarf.remove(liar)

dwarf.sort()

for d in dwarf:
    print(d)