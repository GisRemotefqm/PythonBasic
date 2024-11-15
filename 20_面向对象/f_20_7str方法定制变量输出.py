class Human:
    # 初始化函数
    def __init__(self, human_name,human_age):
        print("初始化了")
        self.name = human_name
        self.age = human_age

    # self 是对象的引用，谁调用的就是谁的引用
    def run(self):
        print("%s开始跑步了" % self.name)
        # pass

    def eat(self):
        print("%s开始吃东西" % self.name)

    def __del__(self):
        print("%s无了" % self.name)

    def __str__(self):
        return "嘿嘿嘿"

# 若不重写__str__函数，print(对象)则会输出对象引用的内存地址
# 重写后，print(对象)会输出重写的内容，但__str__返回值必须是字符串
xm = Human("小明", 17)
print(xm)