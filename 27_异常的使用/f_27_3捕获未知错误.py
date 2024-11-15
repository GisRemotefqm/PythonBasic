# 语法 except Exception as result:
try:
    num = int(input("请输入一个整数"))
    num1 = 8 / num

except Exception as result:

    # 可以通过变量 result 输出具体的错误信息
    print("这个错误是%s" % result)
