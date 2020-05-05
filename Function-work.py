import os
import math
import time

def inputNum():
    try:
        userIn = input("input:")
        intIn = int(userIn)
        return intIn
    except ValueError:
        if userIn == "":
            return "end"
        else:
            print("input error")
            return "error"

if __name__ == '__main__':
    inArray = []
    while True:
        userin = inputNum()
        if userin == "end":
            break
        elif userin == "error":
            pass
        else:
            inArray.append(userin)

inSum = sum(inArray)
inAvg = inSum / len(inArray)
insort = inArray[:]
insort.sort()

print(inSum)
print(inAvg)
print(insort)

with open("nums-Func.txt", "w") as f:
    f.write(str(time.time()))
    for i in inArray:
        f.write(str(i)+ "\n")
    
with open("nums-Func.txt") as f:
    for line in f.readlines():                          
        line = line.strip()                             
        if not len(line) or line.startswith('#'):       
            continue                                   
        print(line)           
        
