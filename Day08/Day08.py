answerPart1 = 0
answerPart2 = 0
previousInput = 0
loopCounter = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

for stringCor in content_list:
    splitString = stringCor.split("|")[1]
    stringList = splitString.split()
    for string in stringList:
        if (len(string) == 2 or len(string) == 3 or
            len(string) == 4 or len(string) == 7):
            answerPart1 += 1



print("The answer is of part one is  " + str(answerPart1))
print("The answer is of part two is  " + str(answerPart2))