
name_list = ["zhangsan", "lisi", "wangwu", "wangermazi"]

# 得到列表中的值
print(name_list[0])

# 通过值获取到列表中的索引
print(name_list.index("lisi"))

# 修改列表
name_list[3] = "guierzi"

# 增加列表
name_list.append("王小二")  # 在列表最后追加
name_list.insert(2, "小二郎")  # 在指定位置追加
name_list.extend(["hanpi", "nidie"])  # 在表后追加一个表
print(name_list)
# 删除列表

# 在默认没有参数时，删除最后一个元素
name_list.pop()

# 在有参数时，删除指定索引元素
name_list.pop(3)

# 删除指定元素，在有相同元素时默认删除第一个数据
name_list.remove("王小二");

# 扩展 del 删除元素时是清空指定索引元素的内存
del name_list[1]

# 删除所有元素
name_list.clear()



