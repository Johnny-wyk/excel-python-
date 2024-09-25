#作业 1: 百十个求和
"""
num=123
c=num % 10
print(c)
b=round(num/10%10)
print(b)
a=round(num/100%10)
print(a)
print(c+b+a)
"""
import random
import string

"""
import math
#作业 2 ：格式化输出
r=float(input("请输入半径:"))
circle=math.pi*2*r
v=int(math.pi)*r*r
print("周长为:{:.2f}".format(circle))
print("体积为:{:.2f}".format(v))
"""

"""
phoneNumber=input("请输入电话号码:")
s=phoneNumber.replace(phoneNumber[5:8],"****")
print(s)
"""


print(string.digits)

print(random.choice("123"))

s="123"
a=s.split(',')
print(a)