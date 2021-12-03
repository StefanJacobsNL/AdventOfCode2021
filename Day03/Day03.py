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

# part 2

count = 0
oxygenList = content_list
co2List = content_list
oxygenAnswer = ""
co2Answer = ""

maxListCount = len(oxygenList[0])

while(count < maxListCount):
    if len(oxygenList) > 1:
        zeroCount = len([x for x in oxygenList if x[count] == "0"])
        oneCount = len([x for x in oxygenList if x[count] == "1"])

        if zeroCount > oneCount:
            oxygenList = [x for x in oxygenList if x[count] == "0"]
        elif oneCount > zeroCount:
            oxygenList = [x for x in oxygenList if x[count] == "1"]
        elif oneCount ==  zeroCount:
            oxygenList = [x for x in oxygenList if x[count] == "1"]

    if len(co2List) > 1:
        zeroCountCo2 = len([x for x in co2List if x[count] == "0"])
        oneCountCo2 = len([x for x in co2List if x[count] == "1"])
        if zeroCountCo2 < oneCountCo2:
            co2List = [x for x in co2List if x[count] == "0"]
        elif oneCountCo2 < zeroCountCo2:
            co2List = [x for x in co2List if x[count] == "1"]
        elif oneCountCo2 == zeroCountCo2:
            co2List = [x for x in co2List if x[count] == "0"]

    count +=1 

answerPart2 = int(oxygenList[0], 2) * int(co2List[0], 2)

print("The answer is of part two is: " + str(answerPart2))