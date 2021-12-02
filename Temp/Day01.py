answerPart1 = 0
answerPart2 = 0
previousInput = 0
loopCounter = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

# convert string list to int list
content_list = list(map(int, content_list))

# gets the total amount
amountList = len(content_list)



print("The answer is of part one is  " + str(answerPart1))
print("The answer is of part two is  " + str(answerPart2))