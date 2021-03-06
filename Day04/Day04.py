answer = 0
counter = 2
cardCounter = 1
rowCounter = 1
currentCard = 1
currentRow = 1
currentColumn = 0
found = False
answerCard = ""
lastBingo = 0
doneCards = list();

# read file and convert to string list
with open('input.txt') as f:
    content_list = [line.rstrip() for line in f]

bingoNumbers = list(map(int, content_list[0].split(",")))

amountList = len(content_list)
amountBingoNumbers = len(bingoNumbers)

# Create the cards
while counter < amountList:
    if not content_list[counter]:
        cardCounter += 1
        rowCounter = 1
    else:
        globals()[f"card{cardCounter}Row{rowCounter}"] = list(map(int,content_list[counter].split()))
        rowCounter += 1

    counter += 1

# plays the game
for bingoNumber in bingoNumbers:
    while currentCard < cardCounter + 1:
        while currentRow < 6:
            while currentColumn < 5:
                if globals()[f"card{currentCard}Row{currentRow}"][currentColumn] == bingoNumber:
                    globals()[f"card{currentCard}Row{currentRow}"][currentColumn] = "x"

                currentColumn += 1

            currentRow += 1
            currentColumn = 0


        currentCard += 1
        currentRow = 1
        currentColumn = 0

    currentCard = 1
    currentRow = 1
    currentColumn = 0

    while currentCard < cardCounter + 1:
        while currentRow < 6:
            # checks the rows
            if globals()[f"card{currentCard}Row{currentRow}"].count("x") == 5:
                if(doneCards.count(currentCard) == 0):
                    doneCards.append(currentCard)
                    answerCard = currentCard
                    lastBingo = bingoNumber
                    if(cardCounter == len(doneCards)):
                        found = True
                        break
            
            currentRow += 1

        while currentColumn < 5:
            if (globals()[f"card{currentCard}Row{1}"][currentColumn] == "x" and
                    globals()[f"card{currentCard}Row{2}"][currentColumn] == "x" and
                    globals()[f"card{currentCard}Row{3}"][currentColumn] == "x" and
                    globals()[f"card{currentCard}Row{4}"][currentColumn] == "x" and
                    globals()[f"card{currentCard}Row{5}"][currentColumn] == "x"):
                if(doneCards.count(currentCard) == 0):
                    doneCards.append(currentCard)
                    answerCard = currentCard
                    lastBingo = bingoNumber
                    if(cardCounter == len(doneCards)):
                        found = True
                        break

            currentColumn += 1

        if found == True:
            break

        currentCard += 1
        currentRow = 1
        currentColumn = 0

    if found == True:
        break

    currentCard = 1
    currentRow = 1
    currentColumn = 0


counter = 1

while counter < 6:
    tesst = [e for e in globals()[f"card{answerCard}Row{counter}"] if isinstance(e, int)]
    answer += sum(tesst)
    counter += 1

answer = answer * lastBingo
print("The answer is " + str(answer))
