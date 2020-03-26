'''
@Descripttion: Login teaining
@version: 
@Author: Bend Function
@Date: 2020-03-12 19:35:40
@LastEditors: Bend Function
@LastEditTime: 2020-03-13 18:30:18
'''
print("___sign up____")
uname = input("Pls input user name:")
passwd = input("Pls input password:")
print("___log in____")
unameIn = input("Pls input user name:")
passwdIn = input("Pls input password:")
if uname == unameIn and passwd == passwdIn:
    print("login success")
else:
    print("login error")
