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

    # 父类的方法实现不能满足子类的需求时
    # 可以将父类方法重写
    def dark(self):
        print("哈萨克")

        # 可以通过super()方法调用父类的对象
        super().dark()


xtq = GoldDog()
xtq.dark()