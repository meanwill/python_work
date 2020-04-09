maxN, x, y = map(int,input().split(','))

matrix = [[]]
num = 1
for lx in range(x):
    matrix.append([])
    for ly in range(0,y):
        matrix[lx][ly] = num
        num += 1

print(matrix)