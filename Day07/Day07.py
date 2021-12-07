answerPart1 = 0
answerPart2 = 0
fuel = 0
currentfuel = 0
position = 1
counter = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = f.read()

# splits the string and converts it to a int list
content_list = [int(x) for x in content_list.split(",")]

# gets the total amount
amountList = len(content_list)

while (counter < amountList):
    for number in content_list:
        if number > position :
            currentfuel += (number - position)
        elif number < position :
            currentfuel += (position - number)

    if currentfuel < fuel:
        fuel = currentfuel
    elif counter == 0:
        fuel = currentfuel

    counter += 1
    position += 1
    currentfuel = 0

answerPart1 = fuel


print("The answer is of part one is  " + str(answerPart1))
print("The answer is of part two is  " + str(answerPart2))