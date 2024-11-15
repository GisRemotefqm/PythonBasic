# 需求
# 既不需要访问实例属性或调用实例方法
# 也补血药访问类属性或调用类方法时
# 使用静态方法
class Tool:

    @staticmethod
    def print_str():
        print("这是一个静态方法")


# 调用方式，不需要创建对象
Tool.print_str()

