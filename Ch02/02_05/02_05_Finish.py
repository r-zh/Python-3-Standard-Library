# Itertools
import itertools

# Infinite Counting
for x in itertools.count(50, 5): # count from 50, next number is 50 + 5 * i
    print(x)
    if x == 80:
        break;

x = 0;
# Infinite Cycling
for c in itertools.cycle([1, 2, 3, 4]): # cycle means it can go from end to the beginning
    print(c)
    x = x + 1
    if x > 50:
        break;

# Infinite Repeating
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x > 100:
        break;