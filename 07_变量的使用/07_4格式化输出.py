"""
格式化字符    %s    字符串类型
            %d    表示十进制的整数，%06d表示输出整数的显示位数
            %f    浮点数，%0.2f表示输出小数点后两位的整数
            %%    输出%
"""
name = input("请输入你的名字：")
print("%s" %name)
age = int(input("请输入年龄："))
print("%03d" %age)
height = float(input("请输入身高："))
print("%0.3f" %height)
print("%d%%" %25)
print("姓名：%s,年龄：%03d,身高：%0.2f" %(name,age,height))