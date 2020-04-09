maxN, y, x = map(int,input().split(','))

num = 1
lx = 0
while True:
    lx += 1
    for ly in range(y):
        print(num, end="")
        num += 1

    print(matrix[lx])

# print(matrix)