f = open("input.txt", "r")
content = f.read()

x = content.replace(" ", " ")
x = x.split("\n")

list = []
tempList = []

for lines in x:
    for items in lines:
        tempList.append(items)
    list.append(tempList)
    tempList = []



def checksSymbol(item):
    result = 1
    if item != "." and item != "0" and item != "1" and item != "2" and item != "3" and item != "4" and item != "5" and item != "6" and item != "7" and item != "8" and item != "9":
        return result
    return 

def checkGrid(rows, columns):
    """check row before item"""
    foundNumbers = 0
    returnList = [1]
    try:
        if checkNumber(list[rows - 1][columns - 1]) == 1:
            returnList.append(rows - 1)
            returnList.append(columns - 1)
            foundNumbers = 1
    except Exception:
        pass
    try:
        if checkNumber(list[rows -1][columns]) == 1:
            if checkNumber(list[rows - 1][columns - 1]) == None:
                returnList.append(rows - 1)
                returnList.append(columns)
                foundNumbers = 1
    except Exception:
        pass
    try:
        if checkNumber(list[rows - 1][columns + 1]) == 1:
            if checkNumber(list[rows -1][columns]) == None:
                if foundNumbers == 0:
                    returnList.append(rows - 1)
                    returnList.append(columns + 1)
                    foundNumbers = 1
                    
                else:
                    returnList.append(rows - 1)
                    returnList.append(columns + 1)
                    return returnList
    except Exception:
        pass

    """check row in item"""
    try:
        if checkNumber(list[rows][columns - 1]) == 1:
            if foundNumbers == 0:
                returnList.append(rows)
                returnList.append(columns - 1)
                foundNumbers = 1
            else:
                returnList.append(rows)
                returnList.append(columns - 1)
                return returnList
    except Exception:
        pass
    try:
        if checkNumber(list[rows][columns + 1]) == 1:
            if foundNumbers == 0:
                returnList.append(rows)
                returnList.append(columns + 1)
                foundNumbers = 1
            else:
                returnList.append(rows)
                returnList.append(columns + 1)
                return returnList
    except Exception:
        pass

    """check row after item"""
    try:
        if checkNumber(list[rows + 1][columns - 1]) == 1:
            if foundNumbers == 0:
                returnList.append(rows + 1)
                returnList.append(columns - 1)
                foundNumbers = 1
            else:
                returnList.append(rows + 1)
                returnList.append(columns - 1)
                return returnList
    except Exception:
        pass
    try:
        if checkNumber(list[rows + 1][columns]) == 1:
            if checkNumber(list[rows + 1][columns - 1]) == None:
                if foundNumbers == 0:
                    returnList.append(rows + 1)
                    returnList.append(columns)
                    foundNumbers = 1
                else:
                    returnList.append(rows + 1)
                    returnList.append(columns)
                    return returnList
    except Exception:
        pass
    try:
        if checkNumber(list[rows + 1][columns + 1]) == 1:
            if checkNumber(list[rows + 1][columns]) == None:
                if foundNumbers == 0:
                    returnList.append(rows + 1)
                    returnList.append(columns + 1)
                    foundNumbers = 1
                else:
                    returnList.append(rows + 1)
                    returnList.append(columns + 1)
                    return returnList
    except Exception:
        pass
    return


def checkNumber(tempitem):
    result = 1
    if tempitem == "0" or tempitem == "1" or tempitem == "2" or tempitem == "3" or tempitem == "4" or tempitem == "5" or tempitem == "6" or tempitem == "7" or tempitem == "8" or tempitem == "9":
        return result
    return

def checkStar(tempitem):
    result = 1
    if tempitem == "*":
        return result
    return

rows = 0
columns = 0

tempRows = 0
tempColumns = 0
tempNumberString1 = ""
tempNumberString2 = ""

sum = 0


for lines in list:
    while columns < len(list[rows]):
        if checkStar(list[rows][columns]) == 1:
            tempList = checkGrid(rows, columns)
            if tempList != None:
                """Check numbers fist numbers"""
                tempColumns = tempList[2]
                tempRows = tempList[1]
                countDown = 1
                tempNumberString1 = ""
                while countDown == 1:
                    tempColumns = tempColumns - 1
                    if checkNumber(list[tempRows][tempColumns]) == None:
                        tempColumns = tempColumns + 1
                        countDown = 0
                tempNumberString1 = tempNumberString1 + list[tempRows][tempColumns]
                countUp = 1
                while countUp == 1:
                    tempColumns = tempColumns + 1
                    try:
                        if checkNumber(list[tempRows][tempColumns]) == None:
                            tempColumns = tempColumns - 1
                            countUp = 0
                            break
                    except:
                        tempColumns = tempColumns - 1
                        countUp = 0
                        break
                    tempNumberString1 = tempNumberString1 + list[tempRows][tempColumns]
                """end check numbers"""
                """Check numbers second numbers"""
                tempColumns = tempList[4]
                tempRows = tempList[3]
                countDown = 1
                tempNumberString2 = ""
                while countDown == 1:
                    tempColumns = tempColumns - 1
                    if checkNumber(list[tempRows][tempColumns]) == None:
                        tempColumns = tempColumns + 1
                        countDown = 0
                tempNumberString2 = tempNumberString2 + list[tempRows][tempColumns]
                countUp = 1
                while countUp == 1:
                    tempColumns = tempColumns + 1
                    try:
                        if checkNumber(list[tempRows][tempColumns]) == None:
                            tempColumns = tempColumns - 1
                            countUp = 0
                            break
                    except:
                        tempColumns = tempColumns - 1
                        countUp = 0
                        break
                    tempNumberString2 = tempNumberString2 + list[tempRows][tempColumns]
                """end check numbers"""
                sum = sum + (int(tempNumberString1) * int(tempNumberString2))
        columns = columns + 1
    rows = rows + 1
    columns = 0
print(sum)
    