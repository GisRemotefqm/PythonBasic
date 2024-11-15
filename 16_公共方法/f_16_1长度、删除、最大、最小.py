name_str = "zhangsan"
zs_tuple = ("zhangsan", 17, 175.2)
zs_list = [1, 2, 3, 1]
zs_dictory = {"name": "zhangsan",
              "age": 17,
              "height": 185.5}
# 长度
print(len(name_str))
print(len(zs_tuple))
print(len(zs_list))
print(len(zs_dictory))

# del 删除，从内存中删除

# 最大、最小
print((zs_list, [2, 2, 2, 2]))
print(max(name_str, "lisi"))
print(min(zs_tuple, ("lisi", 2, 3)))
