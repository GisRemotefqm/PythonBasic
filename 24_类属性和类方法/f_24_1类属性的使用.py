# 类属性就是给类对象中定义的属性
# 类属性通常记录这个类相关的特征
# 类属性不用于记录对象的具体特征


# 示例
# 创建一个工具类
# 需求-- 知道使用这个类创建了多少个工具对象
class Tool:

    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        # self.count只会在某个对象中出现
        # 也就是对对象的属性
        # self.count += 1

        # Tool.count是对类的属性
        Tool.count += 1


qianzi = Tool("钳子")
banshou = Tool("扳手")
tiesi = Tool("铁丝")
print(Tool.count)

print(qianzi.count)  # 虽然也可以获取到类属性，但不推荐

# 这并不会影响到Tool.count的值，因为相当于self.count = 99
# 并不影响Tool.count的值
qianzi.count = 99

