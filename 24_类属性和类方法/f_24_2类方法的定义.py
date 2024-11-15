# 语法
# def 方法名(cls)

class Tool:
    # 类属性
    count = 0

    def __init__(self):
        Tool.count += 1

    # 类方法,一定要加@classmethod
    @classmethod
    def show_tool_count(cls):

        # 在方法内部
        # 使用  cls.属性 cls.方法调用类属性和类方法
        print("%d" % cls.count)

    @classmethod
    def print_a1(cls):

        # 在类方法中才能调用另一个类方法
        cls.show_tool_count()


a = Tool()
b = Tool()
C = Tool()

Tool.print_a1()