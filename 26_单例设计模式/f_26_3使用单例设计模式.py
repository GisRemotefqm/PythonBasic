# 使用一个类对象接收第一次被初始化后的引用


class Music_Player():
    cls_addr = None

    def __new__(cls, *args, **kwargs):
        if cls.cls_addr is None:

            print("第一次创建实例")
            cls.cls_addr = super().__new__(cls)

        # 不是第一次实例化就直接返回cls_none
        return cls.cls_addr

    def __init__(self, name):
        self.name = name
        print("我被执行了")

player1 = Music_Player("小明")
player2 = Music_Player("s")

print(player2)
print(player1)

if player2 is player1:
    print("是相同的")
