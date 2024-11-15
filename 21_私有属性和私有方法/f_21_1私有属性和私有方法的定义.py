# 私有属性和方法是不想对外公开的属性和方法
# 定义方法在属性或方法前加两个下划线

class Women:
    def __init__(self, name, age):
        # 私有属性
        self.__name = name

        # 公有属性
        self.age = age

    # 公有方法
    def print_self(self):
        print("我的年龄是%d" % self.age)

    # 私有方法
    def __print_name(self):
        print("我的名字叫" % self.__name)


xm = Women("xm", 16)
xm.print_self()

# 私有属性和方法在外界不能直接访问
# python中没有真正意义上的私有,下列方法就可以访问到


xm._Women.__print_name()
print(xm._Women__name)
