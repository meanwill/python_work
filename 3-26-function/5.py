fuckIn = eval(input())

ele = []

for i in range(1,fuckIn):
    if fuckIn % i == 0:
        ele.append(i)

if sum(ele) == fuckIn:
    print("%d="%fuckIn,end="")
    for i in ele:
        if i != ele[len(ele) - 1]:
            print("%d+"%i)
        else:
            print("%d"%i)