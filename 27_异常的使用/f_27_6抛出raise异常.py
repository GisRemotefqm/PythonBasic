# 当代码本身不会出错 但是对某一需求需要处理时
# 例如要求密码长度大于8 本身输入多少个字符都不会出错
# 但是我们要求要大于 8

def input_pwd():
    pwd = input("请输入密码")
    if len(pwd) < 8:
        ex = Exception("密码长度小于8，重新输入")
        raise ex
    return pwd

try:
    print(input_pwd())
except Exception as result:
    print(result)