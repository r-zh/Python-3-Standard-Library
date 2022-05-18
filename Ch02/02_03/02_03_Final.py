# Random Module
import random

# Random Numbers
print(random.random())
decider = random.randrange(2) # from 0 to the parameter number
if decider == 0:
    print("HEADS")
else:
    print("TAILS")
print(decider)

print("You rolled a " + str(random.randrange(1, 7))) # must convert number to string, or error appears

# Random Choices
lotteryWinners = random.sample(range(100), 5) # create a list with 5 numbers in range of 100
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards) # 洗牌
print(cards)