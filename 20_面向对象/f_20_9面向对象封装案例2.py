# 需求
# 房子（Home）有户型、总面积和家具列表名称
# 房子可以添加家具，并输出现在有什么家具
# 家具（HouseItem）有名字、和占地面积


# 家具类
class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.2f" % (self.name, self.area)


# 房子类
class Home:

    # 需要从外部定义的参数使用形参
    # 不需要直接在内部定义
    def __init__(self, house_tpye, area):
        self.house_type = house_tpye
        self.area = area

        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def add_item(self, item):
        if item.area > self.free_area:
            print("%s太大了无法添加" % item.name)
            return
        else:
            self.item_list.append(item.name)
            self.free_area -= item.area

    def __str__(self):

        # python中可以使用小括号将内部代码连接在一起
        return ("户型是%s 总面积是%.2f 剩余面积是%.2f 家具有%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))


xms = HouseItem("xms", 4.5)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 3)

print(xms)
print(chest)
print(table)

my_home = Home("两市一厅", 80)
my_home.add_item(xms)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)