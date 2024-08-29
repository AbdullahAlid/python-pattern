n = 5
output = ""
for i in range(1, n+1):
    for j in range(1, i+1):
        if (i+j) % 2 == 0:
            output += str(1)+" "
        else:
            output += str(0)+" "
    print(output)
    output = ""
