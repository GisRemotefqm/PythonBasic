# 类的命名要满足大驼峰命名法
# 对对象的特征描述就是属性
# 对对象行为的描述就是方法
class Human:

    # name age 是属性
    name = ""
    age = 17

    # run eat 是方法
    # 定义方法：
    # def 函数名(self,参数列表)：


    def run(self):
        print("开始跑步了")
        # pass


    def eat(self):
        print("开始吃东西")
        # pass


# 创建对象
# xm 相当于变量，去引用Human对象的内存地址
xm = Human()
xm.eat()
print(id(xm))
