def demo1():
    print("I am module 1")

text = "module_1"


class Animal:
    pass

# 在模块中使用__name__属性永远返回__main__
# 但在别处会输出模块名
# 所以利用__name__属性判断是否执行测试代码

# 测试代码
def main():
    print(__name__)
    print(text)
    demo1()
#
if __name__ == "__main__":
    main()
