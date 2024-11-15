class Animal:
    def eat(self):
        print("吃")

    def __sleep(self):
        print("睡")

    def play(self):
        self.__sleep()
        print("玩")


class Dog(Animal):

    def dark(self):
        print("aass")

        super().play()
        # 子类无法直接调用父类的私有方法和属性
        # self.__sleep()



# 使用super可以间接的调用父类的公有属性
# 通过公有方法访问私有属性和方法
# 公有方法中有父类私有方法的调用
wangcai = Dog()
wangcai.play()
