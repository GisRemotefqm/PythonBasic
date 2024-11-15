# 返回多个数据
def measure():
    """测量温度"""
    temp = 37
    wetness = 50  # 湿度

    # 等同于下面的元组
    return temp, wetness
    # return (temp,wetness)

result = measure()
print(result)
print(type(result))

# 可以拿出单个数据
print(result[0])
print(result[1])

# 如果返回的类型是元组，又希望单独处理其中的某一个元素
# 可以使用多个变量一次接收返回结果
# 如果使用多个变量接收需要与返回个数一致

gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
print(type(gl_temp))
