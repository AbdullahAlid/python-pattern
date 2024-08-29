n = 4
m = n-1
output = ""
for i in range(n):
    for j in range(n):
        if j < m:
            output += " "
        else:
            output += "*"
    print(output)
    output = ""
    m -= 1
