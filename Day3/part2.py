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
    result = 1
    foundNumbers = 0
    rows1 = 0
    columns1 = 0
    rows2 = 0
    columns2 = 0
    try:
        if checkNumber(list[rows - 1][columns - 1]) == 1:
            rows1 = rows - 1
            columns1 = columns - 1
            foundNumbers = 1
    except Exception:
        pass
    try:
        if checkNumber(list[rows -1][columns]) == 1:
            if checkNumber(list[rows - 1][columns - 1]) == 0:
                rows1 = rows - 1
                columns1 = columns
                foundNumbers = 1
    except Exception:
        pass
    try:
        if checkNumber(list[rows - 1][columns + 1]) == 1:
            if checkNumber(list[rows -1][columns]) == 0:
                if foundNumbers == 0:
                    rows1 = rows - 1
                    columns1 = columns + 1
                    foundNumbers = 1
                else:
                    rows2 = rows - 1
                    columns2 = columns + 1
                    return result, rows1, columns1, rows2, columns2
    except Exception:
        pass

    """check row in item"""
    try:
        if checkNumber(list[rows][columns - 1]) == 1:
            if foundNumbers == 0:
                rows1 = rows
                columns1 = columns - 1
                foundNumbers = 1
            else:
                rows2 = rows
                columns2 = columns - 1
                return result, rows1, columns1, rows2, columns2
    except Exception:
        pass
    try:
        if checkNumber(list[rows][columns + 1]) == 1:
            if foundNumbers == 0:
                rows1 = rows
                columns1 = columns + 1
                foundNumbers = 1
            else:
                rows2 = rows
                columns2 = columns + 1
                return result, rows1, columns1, rows2, columns2
    except Exception:
        pass

    """check row after item"""
    try:
        if checkNumber(list[rows + 1][columns - 1]) == 1:
            if foundNumbers == 0:
                rows1 = rows + 1
                columns1 = columns - 1
                foundNumbers = 1
            else:
                rows2 = rows + 1
                columns2 = columns - 1
                return result, rows1, columns1, rows2, columns2
    except Exception:
        pass
    try:
        if checkNumber(list[rows + 1][columns]) == 1:
            if checkNumber(list[rows + 1][columns - 1]) == 0:
                if foundNumbers == 0:
                    rows1 = rows + 1
                    columns1 = columns
                    foundNumbers = 1
                else:
                    rows2 = rows + 1
                    columns2 = columns
                    return result, rows1, columns1, rows2, columns2
    except Exception:
        pass
    try:
        if checkNumber(list[rows + 1][columns + 1]) == 1:
            if checkNumber(list[rows + 1][columns]) == 0:
                if foundNumbers == 0:
                    rows1 = rows + 1
                    columns1 = columns + 1
                    foundNumbers = 1
                else:
                    rows2 = rows + 1
                    columns2 = columns + 1
                    return result, rows1, columns1, rows2, columns2
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
tempNumberString = ""

sum = 0


for lines in list:
    while columns < len(list[rows]):
        if checkStar(list[rows][columns]) == 1:
            print(checkGrid(rows, columns))
            if checkGrid(rows, columns) == 1:
                print(list[rows][columns])
        columns = columns + 1
    rows = rows + 1
    columns = 0
    