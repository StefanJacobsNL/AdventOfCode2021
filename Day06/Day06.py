answerPart = 0
answerPart2 = 0
maxDays = 256
counter = 0
faseZero = 0
fishDictCounter = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = f.read()

# splits the string and converts it to a int list
content_list = [int(x) for x in content_list.split(",")]

# declares the dictonary
fishDict = {
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0
}

# converts to input into the dictonary
for item in content_list:
    fishDict[item] += 1

while counter < maxDays:
    while fishDictCounter < 8:
        if fishDictCounter == 0:
            faseZero = fishDict[fishDictCounter]

        fishDict[fishDictCounter] = fishDict[fishDictCounter + 1]
        fishDictCounter += 1

    if faseZero > 0:
        fishDict[6] += faseZero
    
    fishDict[8] = faseZero
    counter += 1
    fishDictCounter = 0
    faseZero = 0

counter = 0
for fish in fishDict:
    answerPart += fishDict[counter]
    counter += 1

print("The answer is " + str(answerPart))