import keyword

name_list = ["zhangsan", "lisi", "wangwu", "wangermazi", "zhangsan"]

# len()函数可以统计列表中元素的总数
lon = len(name_list)
print(lon)

# count 方法可以统计某个元素出现的次数
count = name_list.count("zhangsan")
print(count)


# sort() 方法对列表进行排序，其中reverse默认为False
name_list.sort()
print(name_list)

name_list.sort(reverse=True)

# resever() 方法是对列表进行反转
name_list.reverse()

print(len(keyword.kwlist))