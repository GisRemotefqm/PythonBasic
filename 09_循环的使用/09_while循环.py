"""
whlie 的基本语法
while 条件(判断 计数器 是否达到 目标次数)：
    执行重复的事
    处理条件(计数器变化)
"""
i = 0
result = 0
while i <= 100:

    if i % 2 == 0:
        result += i
    i = i + 1
print(result)
