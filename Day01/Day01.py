increaseCounterPart1 = 0
increaseCounterPart2 = 0
previousInput = 0
loopCounter = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

# convert string list to int list
content_list = list(map(int, content_list))

# gets the total amount
amountList = len(content_list)

# part 1
for item in content_list:
	if previousInput != 0:
		if item > previousInput:
			increaseCounterPart1 += 1
	previousInput = item

previousInput = 0

# part 2
for item in content_list:
	if (loopCounter + 2) < amountList:

		# create the total value
		currentTotal = item + content_list[loopCounter + 1] + content_list[loopCounter + 2]
		
		if previousInput != 0:
			if currentTotal > previousInput:
				increaseCounterPart2 += 1

		# set previous input
		previousInput = currentTotal
	
	loopCounter += 1

print("The answer is of part one is  " + str(increaseCounterPart1))
print("The answer is of part two is  " + str(increaseCounterPart2))