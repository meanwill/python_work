fuckIn = input().split()

a = []
for i in range(0,len(fuckIn)):
    try:
        fuckIn[i] == str(int(fuckIn[i]))
        a.append(int(fuckIn[i]))
    except:
        pass
min = min(a)

print("min = %d"%min)