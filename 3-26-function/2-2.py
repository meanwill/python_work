def fun1(profit):
    bonus_1 = 100000 * 0.1
    bonus_2 = (200000 - 100000) * 0.075 + bonus_1
    bonus_3 = (400000 - 200000) * 0.05 + bonus_2
    bonus_4 = (600000 - 400000) * 0.03 + bonus_3
    bonus_5 = (1000000 - 600000) * 0.015 + bonus_4
    bonus_6 = (profit - 1000000) * 0.01 + bonus_5
    if profit < 0:
        print("0")
    elif profit <= 100000:
        bonus = profit * 0.1
        return bonus
    elif profit <= 200000:
        bonus = (profit - 100000) * 0.075 + bonus_1
        return bonus
    elif profit <= 400000:
        bonus = (profit - 200000) * 0.05 + bonus_2
        return bonus
    elif profit <= 600000:
        bonus = (profit - 400000) * 0.03 + bonus_3
        return bonus
    elif profit <= 1000000:
        bonus = (profit - 600000) * 0.015 + bonus_4
        return bonus

    else:
        bonus = (profit - 1000000) * 0.01 + bonus_5
        return bonus

def fun2(fuckIn):


    total = 0

    if fuckIn < 10 ** 5:
        total = fuckIn * 0.1
    elif fuckIn < 2 * 10 ** 5:
        total = 10 ** 4 + (fuckIn - 10 ** 5) * 0.075
    elif fuckIn < 4 * 10 ** 5:
        total = 10 ** 4 + 10 ** 5 * 0.075 + (fuckIn - 2 * 10 ** 5) * 0.05
    elif fuckIn < 6 * 10 ** 5:
        total = 10 ** 4 + 10 ** 5 * 0.075 + 2 * 10 ** 5 * 0.05 + (fuckIn - 4 * 10 ** 5) * 0.03
    elif fuckIn < 10 ** 6:
        total = 10 ** 4 + 10 ** 5 * 0.075 + 2 * 10 ** 5 * 0.05 + 2 * 10 ** 5 * 0.03 + (fuckIn - 6 * 10 ** 5) * 0.015
    else:
        total = 10 ** 4 + 10 ** 5 * 0.075 + 2 * 10 ** 5 * 0.05 + 2 * 10 ** 5 * 0.03 + 4 * 10 ** 5 * 0.015 + (fuckIn - 10 ** 6) * 0.01

    return total


for i in range(10 ** 5, 10 ** 8, 10):
    if fun1(i) != fun2(i):
        print(i)
        print(fun1(i))
        print(fun2(i))
        exit()
