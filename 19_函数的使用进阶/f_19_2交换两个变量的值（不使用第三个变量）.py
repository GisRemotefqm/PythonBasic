a = 78
b = 96

# 解法1 使用其他变量
c = a
a = b
b = c

# 解法2 不使用其他变量
a = a + b
b = a - b
a = a - b

# 解法3 python中的方法
# 是使用元组进行变量的交换
a, b = (b, a)
# a, b = b, a