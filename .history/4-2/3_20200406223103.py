maxN, y, x = map(int,input().split(','))

matrix = [[]]
num = 1
while True:
    lx += 1
    matrix.append([])
    for ly in range(y):
        matrix[lx].append(num)
        num += 1

    print(matrix[lx])

# print(matrix)