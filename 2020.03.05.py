'''
uesr: 网络193 郑锦凌
time: 2020.03.05
date: 三角形的判断
'''

a = int(input("输入三角形边长:"))
b = int(input("输入三角形边长:"))
c = int(input("输入三角形边长:"))
if (a+b > c and b+c > a and a+c > b) and (a-b < c and a-c < b and  b-c > a):
    if a == b or b == c or c == a:
        print ("等腰三角形")
    elif a*a+b*b == c*c or b*b+c*c ==a*a or a*a+c*c == b*b:
        print("直角三角形")
    else:
        print("普通三角形")
else:
    print("三角形不成立")  

'''
date: 楼层

'''

o = int(input("楼房层数"))
if  (o > 6):
     print("高楼")
else:
     print("低层楼房") 


'''
date:购房税

'''

q = int(input("购房面积"))
if (q >= 140):
    print("征收3%的契税")
else:
    print("征收1%的契税")

