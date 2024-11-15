class Human:
    # 初始化函数
    def __init__(self, human_name, human_age):
        print("初始化了")
        self.name = human_name
        self.age = human_age

    # self 是对象的引用，谁调用的就是谁的引用
    def run(self):
        print("%s开始跑步了" % self.name)
        # pass

    def eat(self):
        print("%s开始吃东西" % self.name)


xm = Human("xiaoming", 18)  # 在创建对象时将属性参数传入
xm.run()
