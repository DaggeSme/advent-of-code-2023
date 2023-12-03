f = open("input.txt", "r")
content = f.read()

x = content.replace(" ", " ")
x = x.split("\n")


def check(lines):
    game = ""
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
                    if int(b[0]) > 14:
                        result = 0
                        return result
                if b[1] == "green":
                    if int(b[0]) > 13:
                        result = 0
                        return result
                if b[1] == "red":
                    if int(b[0]) > 12:
                        result = 0
                        return result
    return game
                    


y = ""
z = ""
a = ""
b = ""
sum = 0
for lines in x:
    sum = sum + int(check(lines))
    print(sum)

