# python 中变量和数据是分开存储的
# 变量中储存的是数据的内存地址
a = 1
b = a
print(id(a))
print(id(b))