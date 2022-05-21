# Getting more control over formatting
from datetime import datetime

now = datetime.now()

# a -> Mon, Tues, Wed
# A -> Monday, Tuesday, Wednesday
# d -> the day in the month, 1, 2, ... 31
# b -> Jan, Feb
# B -> January, Feburary
# m -> the month in the year 1 ... 12
print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%A %B %d"))

# H hour M minute S second P am/pm
print(now.strftime("%H : %M : %S %p"))

# y -> year of last 2 number, Y full year number
print(now.strftime("%y %Y"))
