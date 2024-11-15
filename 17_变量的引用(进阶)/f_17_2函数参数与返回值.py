# 函数中传入的不是数而是数的地址
# 返回值 返回的也是变量的地址
num = 1

print("num的地址是%d" % id(num))

# 向函数中传入参数并查看其指向数据的内存地址
def print_num(a):
    print("a的地址是%d" % id(a))

print_num(num)

def return_address():
    sum = 12
    print("sum的地址是%d" % id(sum))
    return sum

b = return_address()
print("b的地址是%d" % id(b))