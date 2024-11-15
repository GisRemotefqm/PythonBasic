# 字典经常同列表一同使用

xxx_dictory = {"name": "张三",
               "age": 17,
               "height": 185.3,
               "gender": True}
xx_dictory = {"name": "李四",
               "age": 18,
               "height": 175.3,
               "gender": False}

xx_list = [xx_dictory, xxx_dictory]

for my_list in xx_list:
    print(my_list)