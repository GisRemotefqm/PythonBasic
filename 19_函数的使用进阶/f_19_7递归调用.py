# 特点：内部代码是相同的且有参数
# 要有出口否则会死循环
def sum_number(num):

    if num == 1:
        # 这里一定要返回1
        # 第一次执行时为3 到return时重新调用sum_number
        # 此时的参数值为 2
        # 第二次执行参数值为 2,return时为1
        # ...
        # 执行了num 次时 参数值为 num = 1，此时返回1
        # 到num - 1次，返回值1 + 2
        # ...
        # 1 + 2 + 3
        return 1

    temp = sum_number(num-1)
    # print(temp)
    print(type(temp))
    return num + temp

print(sum_number(100))