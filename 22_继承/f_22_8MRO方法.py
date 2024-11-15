# MOR方法是内置方法__mro__()
class A:
    def print_hello(self):
        print("a--hello")


class B:
    def print_hello(self):
        print("b--hello")


# 多继承语法
# class 类名(父类1，父类2)
class C(A, B):

    pass

c = C()
# 可以查看类中方法的执行循序
print(C.__mro__)



