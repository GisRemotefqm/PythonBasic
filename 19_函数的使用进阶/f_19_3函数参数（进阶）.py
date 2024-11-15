# 对于可变和不可变类型
def demo(num, num_list):
    print("开始执行")

    # 在函数中重新不可以对全局变量直接赋值
    # 相当于在函数中重新引用其他数据，并不会对全局变量进行更改
    # 但可变类型使用内部方法会修改外部变量
    num = 11
    num_list.append(9)
    num_list = [4, 5, 6]

    print("num的值为%d" % num)
    print(num_list)
    print("执行结束")

# 定义可变类型和不可变类型的变量
my_num = 99  # 不可变类型
my_list = [1, 2, 3]  # 可变类型

demo(my_num, my_list)
print("my_num = %d" % my_num)
print(my_list)