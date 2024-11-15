# 子类对象调用父类的方法，产生不同的结果
# 就是子类重写了父类的方法
# 多态的重点是不同的对象对父类方法重写叫多态
class Animal:
    def sleep(self):
        print("睡觉了")


class Dog:

    def sleep(self):
        print("躺着睡")


class Cat:
    def sleep(self):
        print("趴着睡")


wangcai = Dog()

wangcai = Animal()
wangcai.sleep()
