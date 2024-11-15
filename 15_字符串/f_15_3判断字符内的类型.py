str = "    \t\n\r"

# string.isspace()用来判断字符中是否只包含空格 \n,\t,\r等
print(str.isspace())

# 判断字符串中是否只包含数字
num_str = "1523"
# unicode 字符串 num_str = "\00b2"
print(num_str)
# 不能判断小数

# 只能判断数字
print(num_str.isdecimal())

# 能判断数字、(1)、 unicode字符数字
print(num_str.isdigit())

# 可以判断数字、汉字数字
print(num_str.isnumeric())