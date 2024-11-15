hello_str = "hello world hello world"

# 拆分字符串，若未给定值则在有空白字符处拆分
str_list = hello_str.split(" ")
for info in str_list:
    print(info)

# 字符串拼接
print("o".join(str_list))

