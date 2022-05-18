# Math Module Part I

import math

# Constants
print(math.pi)
print(math.e)

print(math.nan) # not a number
print(math.inf)
print(-math.inf)

# Trigonometry
obst_direction = math.cos(math.pi / 4)
print(obst_direction)
print(math.sin(math.pi / 4))

# Ceiling and Floor
cookies = 10.3
candy = 7
print(math.ceil(cookies)) # 11, up to next integer if exist decimal point
print(math.ceil(candy))

age = 47.9
otherAge = 47
print(math.floor(age)) # 47, down to last integer if exist decimal point
print(math.floor(otherAge))