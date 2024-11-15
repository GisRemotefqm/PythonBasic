# 如果某个函函数中的代码出错了
# 不会立即抛出异常
# 而是向上寻找调用方直至主函数
# 如果没有异常处理才会抛出异常
def demo1():
    print(ssd)

def demo2():
    return demo1()

# 可以在主程序中去捕获异常
try:
    demo2()
except Exception as result:
    print(result)