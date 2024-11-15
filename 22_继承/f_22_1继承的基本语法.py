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





# 子类可以使用父类的公共属性和方法
wangcai = Dog()
wangcai.sleep()