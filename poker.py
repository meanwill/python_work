#By: Bend Function
import random

def shufflecard(pokers):
    random.shuffle(pokers)
    return pokers

def create():
    no = [_ for _ in range(52)]
    flwNum = 0
    for i in range(len(no)):
        no[i] = suit[flwNum] + d[i%13]
        if i%13==12:
            flwNum += 1
    # print(no)
    return no

def deal(pokers, n):
    humPokers = ""
    for i in range(5):
        if i != 4:
            humPokers += pokers[n - 1 + i * 4] + ","
        else:
            humPokers += pokers[n - 1 + i * 4]

    print("第%d个玩家拿到的牌是：%s"%(n,humPokers))   

suit=['♥','♠','♦','♣']
d=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
n=int(input())
random.seed(n)
poker=create()
poker=shufflecard(poker)
for i in range(52):
    print('%-4s'%poker[i],end='  ')
    if i%13==12:
        print()
for i in range(1,5):
    deal(poker, i)
    
