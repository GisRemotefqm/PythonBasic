# 语法 from 模块名 import 工具名 (as 别名)
# 当导入的两个或多个模块的工具名相同时后导入的会覆盖先导入的
# 此时可以起别名区分
from Module_1 import demo1 as md_1_demo1
from Module_2 import demo1

demo1()
md_1_demo1()
