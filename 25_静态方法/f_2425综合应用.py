# 需求
# 创建Game类，记录最高分，显示帮助信息，开始当前游戏

# 最高分与每次创建的对象无关是类属性
# 帮助信息不需要其他的 属性 方法 是静态类

class Game:
    # 最高分
    highest = 0

    def __init__(self, name):
        self.play_name = name

    def start_game(self):
        print("开始打游戏了")
        print("现在的分数是")

    # 使用类方法显示最高分
    @classmethod
    def show_highest(cls):

        print("最高分是%d" % cls.highest)

    # 使用静态方法显示帮助信息
    @staticmethod
    def game_help():
        print("我是帮助信息")


Game.game_help()
Game.show_highest()
zhangsan = Game("张三")


