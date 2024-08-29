n = 5
output = ""
count = 0
for i in range(1, n+1):
    for j in range(i):
        count += 1
        output += str(count)+" "
    print(output)
    output = ""
