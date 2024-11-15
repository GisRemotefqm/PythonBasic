shi = ["登鹳雀楼",
       "王之涣",
       "白日依山尽",
       "黄河入海流",
       "欲穷千里目",
       "更上一层楼"]

# 左对齐
for poem_str in shi:
    print("%s" % poem_str.ljust(10, " "))

# 右对齐
for poem_str in shi:
    print("%s" % poem_str.rjust(10, " "))

# 居中对齐
for poem_str in shi:
    print("%s" % poem_str.center(10, " "))