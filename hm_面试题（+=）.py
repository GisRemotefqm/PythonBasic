def demo(num, num_list):
    print("函数开始")
    num += num

    # 列表使用 += 本质上是调用extend方法
    num_list += num_list

    # 这个并不会使外部变量改变
    # num_list = num_list + num_list

    print(num)
    print(num_list)
    print("完成")

gl_num = 11
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)