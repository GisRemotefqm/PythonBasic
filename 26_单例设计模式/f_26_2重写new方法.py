class Music_Player():
    def __new__(cls, *args, **kwargs):
        print("调用new方法")

        # 可以使用父类的方法获取对象的内存地址
        addr = super().__new__(cls)

        # 一定要返回内存地址
        # 否则创建对象时不会调用__init__方法

        return addr

    def __init__(self, name):
        self.name = name
        print("我被执行了")


xm = Music_Player("小明")

print(xm)