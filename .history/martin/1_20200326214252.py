string = input()
fin = input()
ty = string.find(fin)
if ty == -1:
    print('can\'t find letter '+ str(fin))
else:
    print('index='+str(ty+1))