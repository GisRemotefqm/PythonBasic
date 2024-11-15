"""
input()函数是得到的是string类型的字符串
"""

price = float(input("请输入价格："))
weight = float(input("请输入重量"))
money = price * weight
# money = float(price) * float(weight)
print(money)