# 在有某个函数传入的参数不确定时使用多值参数
# 可以是接收任意多个参数

# 多值参数的命名：
# 使用字典时 **参数名
# 使用元组时 *参数名

# 但是定义时不是多值参数要定义在前
def demo(abc, *num, **num_1):
    print(abc)
    print(num)
    print(num_1)


demo(1)
print("*"*50)
demo(1, 2, 3, 4)
print("*"*50)
demo(1, 2, 3, 4, name="xiaoming")

# 也可直接使用元组传入，但比较麻烦
def sum_num(*num):
    result = 0
    for my_num in num:
        result += my_num

    print(result)


sum_num(1, 2, 5, 6, 7, 9)
