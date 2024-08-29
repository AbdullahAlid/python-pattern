output = ""
for i in range(4):
    for j in range(5):
        if i == 0 or i == 3:
            output += "*"
        elif j == 0 or j == 4:
            output += "*"
        else:
            output += " "
    print(output)
    output = ""
