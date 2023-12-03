f = open("input.txt", "r")
content = f.read()

x = content.replace(" ", " ")
x = x.split("\n")


def check(lines):
    game = ""
    highBlue = 0
    highGreen = 0
    highRed = 0
    high = []
    y = lines.split(":")
    for lines in y:
        z = lines.split(";")
        for lines in z:
            a = lines.split(",")
            for lines in a:
                lines = lines.strip()
                b = lines.split(" ")
                result = 1
                if b[0] == "Game":
                    game = b[1]
                if b[1] == "blue":
                    if int(b[0]) > highBlue:
                        highBlue = int(b[0])
                if b[1] == "green":
                    if int(b[0]) > highGreen:
                        highGreen = int(b[0])
                if b[1] == "red":
                    if int(b[0]) > highRed:
                        highRed = int(b[0])
    high.append(highBlue)
    high.append(highGreen)
    high.append(highRed)
    return high
                    


sum = 0
tempList = []
for lines in x:
    tempList = check(lines)
    print(tempList)
    sum = sum + (tempList[0] * tempList[1] * tempList[2])
print(sum)
