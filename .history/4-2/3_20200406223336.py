maxN, y, x = map(int,input().split(','))
#Fuck X
num = 1
lx = 0
while True:
    lx += 1
    for ly in range(y):
        print(num, end="\t")
        num += 1
        if num > maxN:
            exit()

    print()
