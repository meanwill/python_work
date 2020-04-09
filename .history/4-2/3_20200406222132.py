maxN, x, y = map(int,eval(input()).split(" "))

matrix = [[]]
num = 1
for lx in x:
    for ly in y:
        matrix[lx][ly] = num
        num += 1

print(matrix)