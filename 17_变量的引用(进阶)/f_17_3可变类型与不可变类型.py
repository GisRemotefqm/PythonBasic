# 不可变类型 int bool float complex long(2.x)
# 可变类型 list dictory
# 可变与不可变只得是内存中的数据是否可以被修改
# 可变的：修改后内存地址不会被修改
# 不可变：只得是修改后内存地址也会被改变
my_list = [1, 2, 3]
print("修改前list的地址为%d" % id(my_list))

# 只有调用方法时地址不会改变
my_list.extend([4, 5])

print("修改后list的地址为%d" % id(my_list))

# 对list重新赋值后地址会改变
my_list = [1, 2, 3]
print("重新赋值后的list地址%d" % id(my_list))

# 字典是通过 key 值进行修改
# 并且字典中的 key 值必须是不可变类型
# 因为如果是可变类型若因某些操作将 key 修改 key 值可能不唯一
my_dict = {"name": "小明",
           "age": 17}
print("修改前字典的地址是%d" % id(my_dict))

my_dict["name"] = "小晓明"
print("修改后的内存地址是%d" % id(my_dict))

# 哈希函数 hash()只能接收不可变类型
# 相同的内容可以得到相同的结果
# 不同的内容会得到不同的结果