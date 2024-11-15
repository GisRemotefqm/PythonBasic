class Human:
    # 初始化函数
    def __init__(self):
        print("初始化了")
        self.name = "xm"
        self.age = 18

    # self 是对象的引用，谁调用的就是谁的引用
    def run(self):
        print("%s开始跑步了" % self.name)
        # pass

    def eat(self):
        print("%s开始吃东西" % self.name)

xm = Human()  # 这时就已经完成了初始化函数的调用
# xm.run()