select_name = "wangwu"
xxx_list = [ {"name":"zhangsan",
                       "age":17,
                       "height":185.2},
             {"name": "lisi",
                       "age": 17,
                       "height": 185.2}
            ]

for my_dictory in xxx_list:
    if my_dictory["name"] == select_name:
        print("找到了%s" % select_name)
        break
# 只有在循环全部完成时才会执行else
else:
    print("没有找到 %s" % select_name)
print("循环结束")