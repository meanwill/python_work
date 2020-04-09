maxN, x, y = map(int,input().split(','))

matrix = [[]]
num = 1
for lx in range(x):
    for ly in range(y):
        matrix[lx][ly] = num
        num += 1

print(matrix)