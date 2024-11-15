# 导入的包可以在Linux中中使用ipython中进行查看
# 在模块名称后加.后按tab键进行查看
import random
player = int(input("请输入您要出的拳：1.石头、2.剪刀、3.布"))
computer = random.randint(1,3)
print("玩家出的拳是 %d - 电脑出的拳是%d" %(player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("你赢了")
elif player == computer:
    print("平手哦")
else:
    print("你输了")