class A:
    def print_a(self):
        print("a")


class B:
    def print_b(self):
        print("b")


# 多继承语法
# class 类名(父类1，父类2)
class C(A, B):
    pass


c = C()
c.print_a()

