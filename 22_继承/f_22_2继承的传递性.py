# 子类继承父类的方法与属性
class Animal:
    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    def play(self):
        print("玩")


class Dog(Animal):

    def dark(self):
        print("aass")


class GoldDog(Dog):
    def fly(self):

        print("我会飞")


# 子类的子类可以使用上一代的方法
xtq = GoldDog()
xtq.fly()
xtq.dark()