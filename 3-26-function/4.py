fuckIn = eval(input())

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
elif fuckIn > 10 ** 6:
    total = 10 ** 4 + 10 ** 5 * 0.075 + 2 * 10 ** 5 * 0.05 + 2 * 10 ** 5 * 0.03 + 4 * 10 ** 5 * 0.015 + (fuckIn - 10 ** 6) * 0.01

print("%.1f"%total)