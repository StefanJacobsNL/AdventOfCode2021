answerPart1 = 0
answerPart2 = 0
fuelPart1 = 0
fuelPart2 = 0
currentfuelPart1 = 0
currentfuelPart2 = 0
position = 1
counter = 0
numberDict = dict()

# read file and convert to string list
with open('input.txt') as f:
    content_list = f.read()

# splits the string and converts it to a int list
content_list = [int(x) for x in content_list.split(",")]

# gets the total amount
amountList = len(content_list)

while (counter < amountList):
    for number in content_list:
        numberFuel = 0
        if number > position :
            currentfuelPart1 += (number - position)
            currentfuelPart2 += sum(range(0, (number - position) + 1 ))
            numberFuel = (number - position)
        elif number < position :
            currentfuelPart1 += (position - number)
            currentfuelPart2 += sum(range(0, (position - number) + 1 ))
            numberFuel = (position - number)

    if currentfuelPart1 < fuelPart1:
        fuelPart1 = currentfuelPart1
    elif counter == 0:
        fuelPart1 = currentfuelPart1

    if currentfuelPart2 < fuelPart2:
        fuelPart2 = currentfuelPart2
    elif counter == 0:
        fuelPart2 = currentfuelPart2

    counter += 1
    position += 1
    currentfuelPart1 = 0
    currentfuelPart2 = 0

answerPart1 = fuelPart1
answerPart2 = fuelPart2


print("The answer is of part one is  " + str(answerPart1))
print("The answer is of part two is  " + str(answerPart2))