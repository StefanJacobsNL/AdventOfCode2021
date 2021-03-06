answerPart1 = 0
answerPart2 = 0
horizontal = 0
vertical = 0
aim = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

# part 1
for item in content_list:
    newWay = item.split(" ")[0]
    newAmount = int(item.split(" ")[1])
    
    if newWay == "forward":
        horizontal += newAmount
    elif newWay == "down":
        vertical += newAmount
    elif newWay == "up":
        vertical -= newAmount

answerPart1 = horizontal * vertical

print("The answer is of part one is  " + str(answerPart1))

# part 2
horizontal = 0
vertical = 0

for item in content_list:
    newWay = item.split(" ")[0]
    newAmount = int(item.split(" ")[1])
    
    if newWay == "forward":
        horizontal += newAmount

        if aim > 0:
            vertical += newAmount * aim
    elif newWay == "down":
        aim += newAmount
    elif newWay == "up":
        aim -= newAmount

answerPart2 = horizontal * vertical

print("The answer is of part two is  " + str(answerPart2))