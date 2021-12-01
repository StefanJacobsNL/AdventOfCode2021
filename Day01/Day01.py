increaseCounter = 0
previousInput = 0

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

# convert string list to int list
content_list = list(map(int, content_list))

for item in content_list:
	if previousInput != 0:
		if item > previousInput:
			increaseCounter += 1
	previousInput = item

print(increaseCounter)