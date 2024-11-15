# 字典的定义
xxx_dictory = {"name": "张三",
               "age": 17,
               "height": 185.3,
               "gender": True}

# 字典的修改
xxx_dictory["name"] = "小张三"
print(xxx_dictory)

# 字典的增加
xxx_dictory["weight"] = 75
print(xxx_dictory)

# 在字典后追加，字典的合并，
# 注意在已有键值对时，若追加已有的，会修改原来的值
xxx_dictory.update({"weight": 65,
                    "remote": "遥感"})
print(xxx_dictory)
# 字典的删除
# pop()方法必须传入参数
xxx_dictory.pop("weight")
print(xxx_dictory)

# 清空字典
xxx_dictory.clear()
print(xxx_dictory)



