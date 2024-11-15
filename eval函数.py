# 将字符串当成有效表达式来求值并返回计算结果

# 基本的计算
# 例：计算器
input_str = eval(input("请输入数学表达式:"))
print(input_str)

# 开发时千万不要使用eval函数直接转换input结果
# 这样会直接创建、删除某些文件
# 例：
__import__('os').system('ls')

# 字符串重复
eval("'*'*50")

# 字符串转换成列表
type(eval("[1, 2, 3]"))

# 字符串转换为字典
type(eval("{name: xiaoming, age: 17}"))