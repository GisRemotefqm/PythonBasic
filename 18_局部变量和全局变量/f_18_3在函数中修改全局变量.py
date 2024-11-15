# 全局变量不允许在函数内部直接修改
num = 1
num1 = 2

def print_num():
    num = 2
    print("num的值为%d" % num)

def print_all():
    global num1
    num1 = 99
    print("num的值为%d" % num)
    print("num1的值为%d" % num1)

def hh():
    print("num1为%d" %num1)

print_num()
print_all()
hh()