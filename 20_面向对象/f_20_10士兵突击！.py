# 需求
# 士兵有一把枪
# 士兵有枪可以开火
# 枪可以发射子弹
# 枪可以装填子弹--增加子弹数量

# ！！！！一个对象的属性可以是另一个类创建的对象

# 有一个士兵类和一个武器类
# 士兵的 属性 士兵姓名、枪
# 士兵的 方法 开火 -- 子弹减少
# 枪的 属性 名字、子弹
# 枪的 方法 装子弹 -- 子弹增多

class Arm:
    def __init__(self, name):
        self.name = name
        self.bullet_number = 0
        # self.bullet_number = bullet_number

    def add_bullet(self, bullet_number):
        self.bullet_number += bullet_number
        print("装弹完毕")

    def shoot(self):
        if self.bullet_number <= 0:
            print("没有子弹了")
            return
        else:
            print("哒哒哒")
            self.bullet_number -= 1

    def __str__(self):
        return "这是一把%s" % self.name



class Soldier:

    def __init__(self, soldier_name, arm):
        self.soldier_name = soldier_name
        self.arm = arm

    def arm_fire(self):
        # 判断None 一般用 is 运算符
        if self.arm is None:
        # if self.arm == None:
            print("无法开火，，，没有武器")

        else:
            self.arm.shoot()
            # 应该定义在枪中
            # self.arm.bullet_number -= 1
            # if self.arm.bullet_number == 0:
                # self.arm.add_bullet()

    def __str__(self):
        return ("我是%s,使用的枪是%s,还剩%d发子弹"
                % (self.soldier_name,
                   self.arm.name,
                   self.arm.bullet_number))





soldier_arm = Arm("ak47")
soldier = Soldier("龙文章", soldier_arm)
soldier.arm.add_bullet(30)
soldier.arm_fire()
soldier.arm_fire()
soldier.arm_fire()

print(soldier)
print(soldier_arm)



