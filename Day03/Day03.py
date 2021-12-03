answerPart1 = 0
answerPart2 = 0
zeroCount = 0
oneCount = 0
gamma = "";
epsilon = "";
count=0

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

stringLength = len(content_list[0])

# part 1
while(count<stringLength):
    for item in content_list:
        if item[count] == "0":
            zeroCount += 1
        elif item[count] == "1":
            oneCount += 1
    
    if zeroCount > oneCount:
        gamma += "0"
        epsilon += "1"
    elif oneCount > zeroCount:
        gamma += "1"
        epsilon += "0"

    zeroCount = 0
    oneCount = 0
    count +=1   

answerPart1 = int(gamma, 2) * int(epsilon, 2)

print("The answer is of part one is: " + str(answerPart1))
print("The answer is of part two is: " + str(answerPart2))