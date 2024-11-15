shi = ["\t登鹳雀楼",
       "王之涣",
       "白日依山尽",
       "黄河入海流\t",
       "欲穷千里目",
       "更上一层楼"]
for poem_str in shi:
    # 使用strip去除空白字符
       print("|%s|" % poem_str.strip().center(10, "　"))