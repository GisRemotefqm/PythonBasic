# 使用多值参数时想将元组或字典直接传给多值参数
# 使用拆包简化参数的传递
# 拆包的方式：
# 元组变量前加 *
# 字典变量前 **
gl_tuple = (1, 2, 3)
gl_dictory = {"name": "xiaoming",
              "age": 17}


def demo(*num_tuple, **name_dict):
    print(num_tuple)
    print(name_dict)


demo(*gl_tuple, **gl_dictory)

# 拆包就相当于将参数以下列方法输入对应的元组和字典
demo(1, 2, 3, name="xm", age=17)
