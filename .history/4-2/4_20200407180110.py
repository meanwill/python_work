
张钰江 4/7/2020 6:00:42 PM
a=list(eval(input('请输入列表元素：')))
print(a)
b=list(input('请输入列表元素：').split(' '))
c=[]
for i in b:
        c.append(eval(i))
print(b)
d=[eval(i) for i in list(input('请输入列表元素:').split(' '))]
print(d)