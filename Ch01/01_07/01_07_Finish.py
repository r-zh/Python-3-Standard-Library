# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters
# split() on the space and create a list
# key= str.upper -> all the items will be upperCase "when" compare
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInaGame, reverse=True))

leaderBoard = {231: "CKL", 123:"ABC", 432:"JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [ ('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
# sort by the first item in each tuple
print(sorted(students, key=lambda student:student[0]))
print(sorted(students, key=lambda student:student[1]))
print(sorted(students, key=lambda student:student[2]))

