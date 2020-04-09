maxN, y, x = map(int,input().split(','))

num = 1
lx = 0
while True:
    lx += 1
    matrix.append([])
    for ly in range(y):
        matrix[lx].append(num)
        num += 1


    print(matrix[lx])

# print(matrix)