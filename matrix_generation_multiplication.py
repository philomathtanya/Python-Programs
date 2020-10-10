def matrixGenMul(firstValue, rows, columns):
    a = []
    b = []
    r = []
    for i in range(rows):
        x = []
        for j in range(columns):
            x.append(firstValue)
            firstValue += 1
        a.append(x)
    for i in range(columns):
        b.append([a[j][i] for j in range(rows)])
    for i in range(rows):
        r.append([0]*rows)
    for i in range(rows):
        for j in range(rows):
            r[i][j] = 0
            for k in range(columns):
                r[i][j] += a[i][k]*b[k][j]
    return r


firstValue = int(input("Enter the first value: "))
rows = int(input("Enter no. of rows of the matrix: "))
columns = int(input("Enter no. of columns of the matrix: "))
print("The required resultant matrix:")
r = matrixGenMul(firstValue, rows, columns)
for i in range(rows):
    for j in range(rows):
        print(r[i][j], end=" ")
    print()
