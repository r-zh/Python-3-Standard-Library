# Statistics Module
import statistics
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(agesData)) # average
print(statistics.mode(agesData)) # most frequent value
print(statistics.median(agesData)) # midpoint
print(sorted(agesData))

print(statistics.variance(agesData)) # the average of the squared differences from the mean
print(statistics.stdev(agesData)) # the square root of variance
print(math.sqrt(statistics.variance(agesData))) # same as above
