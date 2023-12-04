import math

f = open("input.txt", "r")
content = f.read()

x = content.strip()
x = x.split("\n")

WinningNumbers = []
MyNumbers = []
winningTrack = 0
WinningCount = 0
sum = 0
for lines in x:
    lines = lines.split("|")
    for items in lines:
        items = items.strip()
        items = items.replace("  ", " ")
        items = items.split(" ")
        if items[0] == "Card":
            items.pop(0)
            items.pop(0)
        for numbers in items:
            if winningTrack == 0:
                WinningNumbers.append(numbers)
            else:
                MyNumbers.append(numbers)
        winningTrack = 1
        
        for winning in WinningNumbers:
            for my in MyNumbers:
                if winning == "1" and my != "1":
                    pass
                elif winning == "2" and my != "2":
                    pass
                elif winning == "3" and my != "3":
                    pass
                elif winning == "4" and my != "4":
                    pass
                elif winning == "5" and my != "5":
                    pass
                elif winning == "6" and my != "6":
                    pass
                elif winning == "7" and my != "7":
                    pass
                elif winning == "8" and my != "8":
                    pass
                elif winning == "9" and my != "9":
                    pass
                elif winning == "0" and my != "0":
                    pass
                else:
                    if (my.find(winning)) != -1:
                        WinningCount = WinningCount + 1
                        print("Match! ", winning, " ", my)
          
    if WinningCount != 0:
        sum = sum + math.pow(2, (WinningCount - 1))
    WinningCount = 0
    winningTrack = 0
    WinningNumbers = []
    MyNumbers = []  
    
print(sum)