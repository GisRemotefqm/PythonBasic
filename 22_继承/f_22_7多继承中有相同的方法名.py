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
c.print_hello()