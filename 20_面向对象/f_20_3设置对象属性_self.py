class Human:


    # self 是对象的引用，谁调用的就是谁的引用
    def run(self):
        print("%s开始跑步了" % self.name)
        # pass

    def eat(self):
        print("%s开始吃东西" % self.name)
        # pass

xm = Human()
# 在外部定义属性时如果某个函数提前使用了属性就会报错
# xm.run()
# 不推荐使用
xm.name = "xm"
xm.age = 17