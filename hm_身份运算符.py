# 身份运算符用来比较两个对象的内存地址是否一致
# 是否是同一个对象的引用
# 运算符 is 和 not is

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


xm = Person("xm", 18)
wangwu = Person("王五", 45)

xmm = xm

print(xm is xmm)
print(wangwu is xm)
