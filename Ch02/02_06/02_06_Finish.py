# Itertools Part 2
import itertools

# Permutations: Order matters - some copies with same inputs but in different order 排列
election = {1: "Barb", 2:"Karen", 3:"Erin"}
for p in itertools.permutations(election): # all different combination 123 132 321 ....
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter - no copies with same inputs
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colorsForPainting, 4): # only take 4 elements in the list and no repeat
    print(c)