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



def checkSymbol(item):
    result = 1
    if item != "." and item != "0" and item != "1" and item != "2" and item != "3" and item != "4" and item != "5" and item != "6" and item != "7" and item != "8" and item != "9":
        return result
    return 

def checkGrid(rows, columns):
    """check coulmn before item"""
    result = 1
    try:
        if checkSymbol(list[rows - 1][columns - 1]) == 1:
            return result
    except Exception:
        pass
    try:
        if checkSymbol(list[rows][columns - 1]) == 1:
            return result
    except Exception:
        pass
    try:
        if checkSymbol(list[rows + 1][columns - 1]) == 1:
            return result
    except Exception:
        pass

    """check coulmn in item"""
    try:
        if checkSymbol(list[rows - 1][columns ]) == 1:
            return result
    except Exception:
        pass
    try:
        if checkSymbol(list[rows][columns]) == 1:
            return result
    except Exception:
        pass
    try:
        if checkSymbol(list[rows + 1][columns]) == 1:
            return result
    except Exception:
        pass

    """check coulmn after item"""
    try:
        if checkSymbol(list[rows - 1][columns + 1]) == 1:
            return result
    except Exception:
        pass
    try:
        if checkSymbol(list[rows][columns + 1]) == 1:
            return result
    except Exception:
        pass
    try:
        if checkSymbol(list[rows + 1][columns + 1]) == 1:
            return result
    except Exception:
        pass
    return


def checkNumber(tempitem):
    result = 1
    if tempitem == "0" or tempitem == "1" or tempitem == "2" or tempitem == "3" or tempitem == "4" or tempitem == "5" or tempitem == "6" or tempitem == "7" or tempitem == "8" or tempitem == "9":
        return result
    return

rows = 0
columns = 0

tempRows = 0
tempColumns = 0
tempitem = ""
tempNumberString = ""

sum = 0


for lines in list:
    while columns < len(list[rows]):
        tempitem = list[rows][columns]
        if checkNumber(tempitem) == 1:
            if checkGrid(rows, columns) == 1:
                tempColumns = columns
                countDown = 1
                tempNumberString = ""
                while countDown == 1:
                    tempColumns = tempColumns - 1
                    if checkNumber(list[rows][tempColumns]) == None:
                        tempColumns = tempColumns + 1
                        countDown = 0
                
                tempNumberString = tempNumberString + list[rows][tempColumns]
                columns = tempColumns
                countUp = 1
                while countUp == 1:
                    columns = columns + 1
                    try:
                        if checkNumber(list[rows][columns]) == None:
                            columns = columns - 1
                            countUp = 0
                            break
                    except:
                        columns = columns - 1
                        countUp = 0
                        break
                    tempNumberString = tempNumberString + list[rows][columns]
                sum = sum + int(tempNumberString)
        columns = columns + 1
    rows = rows + 1
    columns = 0
print(sum)
    