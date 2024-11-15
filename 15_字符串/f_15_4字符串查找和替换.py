hello_str = "hello world"
str = "hello"

# 判断字符串是否是以 str开头
print(hello_str.startswith(str))

# 判断是否以指定的字符串结束
print(hello_str.endswith(str))

# 查找指定字符串
print(hello_str.find("llo"))
print(hello_str.find("sss"))    # 若没有为 -1

# 替换字符串 但不会修改原有字符串
print(hello_str.replace("hello", "hi"))
print(hello_str)
