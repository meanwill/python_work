'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-03-13 18:30:27
@LastEditors: Bend Function
@LastEditTime: 2020-03-14 19:53:58
'''
import turtle as t
i = int(input("请输入多边形变数："))
# 粗细
t.pensize(3)
#速度
t.speed(10)
a = 360 / i
while i>0:
    t.right(a)
    # 边长
    t.forward(100)
    i -=1
t.done()
