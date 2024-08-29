n = 5
m = n+1
output = ""
for i in range(n):
    for j in range(1, m):
        output += str(j)
    print(output)
    m = m-1
    output = ""
