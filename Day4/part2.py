import math

f = open("input.txt", "r")
content = f.read()

x = content.strip()
x = x.split("\n")

WinningNumbers = []
MyNumbers = []
winningTrack = 0

cardsWinning = []
cardsMyNumbers = []

sum = 0
for lines in x:
    lines = lines.split("|")
    for items in lines:
        items = items.strip()
        items = items.replace("  ", " ")
        items = items.split(" ")
        if items[0] == "Card":
            items.pop(0)
            items[0] = items[0].rstrip(":")
            MyNumbers.append(items[0])
        for numbers in items:
            if winningTrack == 0:
                WinningNumbers.append(numbers)
            else:
                MyNumbers.append(numbers)
        winningTrack = 1
    cardsWinning.append(WinningNumbers)
    cardsMyNumbers.append(MyNumbers)
    winningTrack = 0
    WinningNumbers = []
    MyNumbers = [] 

newCardsWinning = cardsWinning
newCardsMyNumbers = cardsMyNumbers

cardsCount = 0

while cardsCount < len(newCardsWinning):
    print(newCardsWinning[cardsCount])
    cardsCount += 1