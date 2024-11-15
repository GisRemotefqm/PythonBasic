class Person:
    def __init__(self, p_name, p_weight):
        self.weight = p_weight
        self.name = p_name

    def run(self):
        self.weight -= 0.5
        print("我是%s减了0.5公斤，现在的体重是%.2f" % (self.name, self.weight))

    def eat(self):
        self.weight += 1
        print("我是%s吃胖了 1 公斤，现在的体重是%.2f" % (self.name, self.weight))


xmm = Person("小美眉", 50)
xmm.run()
xmm.run()
xmm.eat()
