"""
定义函数：
    def 函数名():
        代码...
定义好函数后，只是表示这个函数封装了一段代码
使用函数需要调用
"""

def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" %(col,row,col * row),end = "\t")
            col += 1
        row += 1
        print("")
