n = 4
m = n
output = ""
for i in range(n):
    for j in range(m):
        output += "*"
    m = m-1
    print(output)
    output = ""
