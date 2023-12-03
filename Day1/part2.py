f = open("input.txt", "r")
content = f.read()

x = content.split("\n")

search = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def findAll(string, what):
    where = 0
    whereList = []
    while where != -1:
        if string.find(what, where) == -1:
            break
        elif string.find(what, where) != -1:
            whereList.append(string.find(what, where))
            where = string.find(what, where) + 1
    if len(whereList) > 0:
        return whereList
    return


def findAllList(string, whatList):
    tempList = []
    multiList = []
    superTempList = []
    for items in whatList:
        tempList = findAll(string, items)
        if tempList != None:
            for numberLocation in tempList:
                if items == "one" or items == "two" or items == "three" or items == "four" or items == "five" or items == "six" or items == "seven" or items == "eight" or items == "nine":
                    items = items.replace("one", "1")
                    items = items.replace("two", "2")
                    items = items.replace("three", "3")
                    items = items.replace("four", "4")
                    items = items.replace("five", "5")
                    items = items.replace("six", "6")
                    items = items.replace("seven", "7")
                    items = items.replace("eight", "8")
                    items = items.replace("nine", "9")
                superTempList = [numberLocation, items]
                multiList.append(superTempList)
    multiList.sort()
    return multiList


tempNumber = ""
FinnalTempList = []
sum = 0
for lines in x:
    FinnalTempList = findAllList(lines, search)
    tempNumber = FinnalTempList[0][1] + FinnalTempList[len(FinnalTempList) - 1][1]
    sum = sum + int(tempNumber)
print(sum)

