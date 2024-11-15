
try:
    num = int(input("请输入一个整数"))
    result = 8 / num
    print(result)
except ValueError:  # 错误1
    print("您输入的不是数字")
except ZeroDivisionError:
    print("分母不能为0")  # 错误2
# except (错误3，错误4)...
