class Music_Player():
    # 接收被创建对象的引用
    cls_addr = None

    # 用来判断是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.cls_addr is None:
            print("第一次创建实例")
            cls.cls_addr = super().__new__(cls)

        # 不是第一次实例化就直接返回cls_none
        return cls.cls_addr

    def __init__(self, name):
        if not Music_Player.init_flag:
            Music_Player.init_flag = True
            self.name = name
            print("我被执行了")
        else:
            return




player1 = Music_Player("小明")
player2 = Music_Player("s")

print(player2)
print(player1)

if player2 is player1:
    print("是相同的")
