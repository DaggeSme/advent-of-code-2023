f = open("input.txt", "r")
content = f.read()


x = content.split("\n")

numbers = []

sum = 0
tempnumber = ""

for lines in x:
    print(lines)
    for chars in lines:
        if chars == "0" or chars == "1" or chars == "2" or chars == "3" or chars == "4" or chars == "5" or chars == "6" or chars == "7" or chars == "8" or chars == "9":
            numbers.append(chars)
    tempnumber = numbers[0] + numbers[len(numbers)-1]
    print(tempnumber)
    sum = sum + int(tempnumber)
    tempnumber = ""
    numbers = []
print(sum)