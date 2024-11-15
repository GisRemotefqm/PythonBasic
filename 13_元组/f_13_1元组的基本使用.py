# 元组定义好后不能修改
info_tuple = ("zhangsan", 11, "wangwu")
print(info_tuple[1])

empty_tuple = ()

# 只包含一个元素的元组,如果不加逗号其类型为元素的变量类型
single_tuple = ("lisi", )
print(type(single_tuple))

# 取值和取索引
info_tuple[1]  # 取值

info_tuple.index("zhangsan")  # 取索引

# 统计计数
info_tuple.count("zhangsan")

# 统计元组中包含的元素个数
len(info_tuple)
