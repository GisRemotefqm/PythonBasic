# 捕获异常
try:

    a = int(input("请输入数字"))
except:
    # 出现错误后执行的代码
    print("哎呀，出错了")

# 出不出错都会正常执行
print("heiheihei")
